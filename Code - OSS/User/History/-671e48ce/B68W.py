from __future__ import annotations

import re

from prompt_toolkit.application import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Dimension, HSplit, Layout, VSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.containers import WindowAlign
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import Frame, TextArea

from agent.config import AppConfig, load_config
from agent.ollama_client import ModelInfo, OllamaClient
from UI.models import ChatEntry


class PromptToolkitTermChat:
    def __init__(self, config: AppConfig | None = None) -> None:
        self.config = config or load_config()
        self.client = OllamaClient(self.config)
        self.entries: list[ChatEntry] = []
        self.models: list[ModelInfo] = []
        self.current_model = self.config.ollama.model
        self.busy = False
        self.status = "Listo. Escribe un mensaje para empezar."

        self.header = FormattedTextControl(text=self._header_text)
        self.status_bar = FormattedTextControl(text=self._status_text)
        self.summary_area = TextArea(read_only=True, scrollbar=False)
        self.models_area = TextArea(read_only=True, scrollbar=True)
        self.transcript_area = TextArea(read_only=True, scrollbar=True, wrap_lines=True)
        self.input_area = TextArea(
            prompt="> ",
            multiline=False,
            wrap_lines=False,
            scrollbar=False,
        )
        self.input_area.buffer.accept_handler = self._on_input_accept

        self.kb = self._build_keybindings()
        self.app = Application(
            layout=Layout(self._build_layout(), focused_element=self.input_area),
            key_bindings=self.kb,
            full_screen=True,
            mouse_support=False,
            style=self._build_style(),
        )

    def _build_style(self) -> Style:
        return Style.from_dict(
            {
                "frame.border": "#5f87af",
                "frame.label": "bold #8fd7ff",
                "header": "bold #ffffff",
                "status": "#8fd7ff",
                "input": "#ffffff",
            }
        )

    def _build_layout(self):
        header_frame = Frame(
            body=Window(self.header, height=2, align=WindowAlign.LEFT),
            title="TermChat",
            style="class:header",
        )
        summary_frame = Frame(self.summary_area, title="Estado")
        models_frame = Frame(self.models_area, title="Modelos")
        top_row = VSplit(
            [summary_frame, models_frame],
            padding=1,
            width=Dimension(weight=1),
            height=Dimension(preferred=8),
        )
        transcript_frame = Frame(self.transcript_area, title="Conversación")
        input_frame = Frame(self.input_area, title="Mensaje")
        footer = Window(self.status_bar, height=1, style="class:status")
        return HSplit(
            [
                header_frame,
                top_row,
                transcript_frame,
                input_frame,
                footer,
            ],
            padding=1,
        )

    def _build_keybindings(self) -> KeyBindings:
        kb = KeyBindings()

        @kb.add("c-q")
        @kb.add("c-c")
        def _quit(_event) -> None:
            self.app.exit()

        @kb.add("f2")
        def _cycle_model(_event) -> None:
            self._cycle_model()

        @kb.add("c-s")
        def _toggle_stream(_event) -> None:
            self.config.ollama.stream = not self.config.ollama.stream
            mode = "on" if self.config.ollama.stream else "off"
            self.status = f"Streaming {mode}."
            self._refresh_ui()

        @kb.add("c-r")
        def _reload_models(_event) -> None:
            self.app.create_background_task(self._refresh_models())

        return kb

    def _header_text(self):
        stream = "on" if self.config.ollama.stream else "off"
        line1 = "class:header", "TermChat  Local Ollama assistant"
        line2 = (
            "",
            f"Modelo activo: {self.current_model}   Stream: {stream}   Host: {self.config.ollama.host}",
        )
        return [line1, ("", "\n"), line2]

    def _status_text(self):
        return [("class:status", f"Estado: {self.status}")]

    def _input_prompt_text(self):
        return [("class:input", "> ")]

    def _sanitize_input(self, raw: str) -> str:
        text = raw
        text = re.sub(r"\x1b\[[0-9;?]*[ -/]*[@-~]", "", text)
        text = re.sub(r"\x1b\].*?(\x07|\x1b\\)", "", text)
        text = re.sub(r"\x1b[^\n\r]*", "", text)
        text = "".join(ch for ch in text if ch == " " or ord(ch) >= 32)
        return text.strip()

    def _on_input_accept(self, _buffer: Buffer) -> bool:
        prompt = self._sanitize_input(self.input_area.text)
        self.input_area.text = ""
        if not prompt:
            return True
        if prompt.startswith(":"):
            self.app.create_background_task(self._handle_command(prompt[1:].strip()))
            return True
        self.app.create_background_task(self._handle_prompt(prompt))
        return True

    async def _handle_command(self, command: str) -> None:
        if command in {"q", "quit", "exit"}:
            self.app.exit()
            return
        if command == "help":
            self.status = "Comandos: :help :models :stream :quit"
            self._refresh_ui()
            return
        if command == "models":
            await self._refresh_models()
            return
        if command == "stream":
            self.config.ollama.stream = not self.config.ollama.stream
            mode = "on" if self.config.ollama.stream else "off"
            self.status = f"Streaming {mode}."
            self._refresh_ui()
            return
        self.status = f"Comando desconocido: :{command}"
        self._refresh_ui()

    async def _handle_prompt(self, prompt: str) -> None:
        self.entries.append(ChatEntry(role="user", content=prompt))
        self.entries.append(ChatEntry(role="assistant", content=""))
        self.busy = True
        self.status = "Consultando Ollama..."
        self._refresh_ui()

        try:
            messages = self._build_messages()
            if self.config.ollama.stream:
                answer = await self._stream_response(messages)
            else:
                answer = await self.client.complete(messages, model=self.current_model)
            self.entries[-1] = ChatEntry(role="assistant", content=answer)
            self.status = "Respuesta recibida."
        except Exception as exc:
            if self.entries and self.entries[-1].role == "assistant" and not self.entries[-1].content:
                self.entries.pop()
            self.status = f"Error: {exc}"
        finally:
            self.busy = False
            self._refresh_ui()

    async def _stream_response(self, messages: list[dict[str, str]]) -> str:
        tokens: list[str] = []
        async for chunk in self.client.stream_chat(messages, model=self.current_model):
            tokens.append(chunk)
            self.entries[-1] = ChatEntry(role="assistant", content="".join(tokens))
            self.status = "Recibiendo streaming..."
            self._refresh_ui()
        return "".join(tokens)

    async def _refresh_models(self) -> None:
        try:
            self.models = await self.client.list_models()
            if self.models and self.current_model not in {m.name for m in self.models}:
                self.current_model = self.models[0].name
            self.status = f"{len(self.models)} modelo(s) disponibles."
        except Exception as exc:
            self.models = []
            self.status = f"No se pudo consultar Ollama: {exc}"
        self._refresh_ui()

    def _cycle_model(self) -> None:
        if not self.models:
            self.status = "No hay modelos cargados."
            self._refresh_ui()
            return
        names = [model.name for model in self.models]
        if self.current_model not in names:
            self.current_model = names[0]
        else:
            idx = names.index(self.current_model)
            self.current_model = names[(idx + 1) % len(names)]
        self.status = f"Modelo activo: {self.current_model}"
        self._refresh_ui()

    def _refresh_ui(self) -> None:
        stream = "on" if self.config.ollama.stream else "off"
        self.summary_area.text = (
            f"Host: {self.config.ollama.host}\n"
            f"Modelo: {self.current_model}\n"
            f"Disponibles: {len(self.models)}\n"
            f"Streaming: {stream}\n"
            f"Mensajes: {len(self.entries)}\n"
            f"Estado: {'Procesando' if self.busy else 'Listo'}"
        )
        if self.models:
            lines = []
            for model in self.models:
                size = (model.size or 0) / (1024**2)
                lines.append(f"{model.name}  {size:.1f} MB")
            self.models_area.text = "\n".join(lines)
        else:
            self.models_area.text = "No hay modelos disponibles."
        self.transcript_area.text = self._format_transcript()
        self.app.invalidate()

    def _format_transcript(self) -> str:
        if not self.entries:
            return "La conversación todavía está vacía."
        parts: list[str] = []
        for entry in self.entries[-self.config.history_limit :]:
            role = entry.role.upper()
            content = entry.content.strip() or "..."
            parts.append(f"{role}:\n{content}")
        return "\n\n".join(parts)

    def _build_messages(self) -> list[dict[str, str]]:
        messages: list[dict[str, str]] = [{"role": "system", "content": self.config.assistant.system_prompt}]
        for entry in self.entries[-self.config.history_limit :]:
            if entry.content:
                messages.append({"role": entry.role, "content": entry.content})
        return messages

    async def run(self) -> None:
        await self._refresh_models()
        self._refresh_ui()
        await self.app.run_async()


async def run() -> None:
    app = PromptToolkitTermChat()
    await app.run()
