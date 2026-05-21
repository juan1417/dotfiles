from __future__ import annotations

import re

from prompt_toolkit.application import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.filters import Condition
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Dimension, HSplit, Layout, VSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.containers import ConditionalContainer, WindowAlign
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import Frame, TextArea

from agent.config import AppConfig, load_config
from agent.ollama_client import ModelInfo, OllamaClient
from UI.models import ChatEntry


SKILL_PRESETS: dict[str, str] = {
    "codigo": "Prioriza soluciones de programacion con pasos claros, ejemplos y buenas practicas.",
    "debug": "Actua como experto en debugging: identifica causa raiz, hipotesis y pruebas minimas.",
    "resumen": "Responde primero con un resumen breve y luego detalles accionables.",
    "explicar": "Explica conceptos complejos con lenguaje simple y ejemplos concretos.",
    "arquitectura": "Enfocate en decisiones de arquitectura, trade-offs y mantenibilidad.",
}


COMMANDS: tuple[str, ...] = (
    "help",
    "models",
    "stream",
    "focus",
    "skills",
    "skill",
    "quit",
    "q",
)


class CommandCompleter(Completer):
    def get_completions(self, document, _complete_event):
        text = document.text_before_cursor
        if not text:
            return
        if not (text.startswith("/") or text.startswith(":")):
            return

        prefix = text[0]
        body = text[1:]
        parts = body.split()
        trailing_space = body.endswith(" ")

        if not parts:
            for cmd in COMMANDS:
                yield Completion(
                    f"{prefix}{cmd}",
                    start_position=-len(text),
                    display=f"{prefix}{cmd}",
                )
            return

        # Complete the command name itself.
        if len(parts) == 1 and not trailing_space:
            current = parts[0]
            start = -len(current)
            for cmd in COMMANDS:
                if cmd.startswith(current):
                    yield Completion(cmd, start_position=start, display=f"{prefix}{cmd}")
            return

        cmd = parts[0]
        # Context-aware completion for /skill <name>
        if cmd == "skill":
            current_arg = "" if trailing_space else parts[-1]
            start = -len(current_arg)
            candidates = list(SKILL_PRESETS.keys()) + ["clear", "off", "none"]
            for candidate in candidates:
                if candidate.startswith(current_arg):
                    yield Completion(candidate, start_position=start, display=candidate)


class PromptToolkitTermChat:
    def __init__(self, config: AppConfig | None = None) -> None:
        self.config = config or load_config()
        self.client = OllamaClient(self.config)
        self.entries: list[ChatEntry] = []
        self.models: list[ModelInfo] = []
        self.current_model = self.config.ollama.model
        self.busy = False
        self.status = "Listo. Escribe un mensaje para empezar."
        self.focus_chat = True
        self.active_skills: list[str] = [
            skill for skill in self.config.assistant.skills if skill in SKILL_PRESETS
        ]

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
        self.input_area.buffer.completer = CommandCompleter()
        # prompt_toolkit expects a callable/filter for `complete_while_typing` in
        # some code paths; provide a callable that returns True to avoid
        # the "'bool' object is not callable" runtime error when typing.
        self.input_area.buffer.complete_while_typing = lambda: True

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
            height=Dimension(min=5, preferred=7, max=9),
        )
        top_row_container = ConditionalContainer(
            content=top_row,
            filter=Condition(lambda: not self.focus_chat),
        )
        transcript_frame = Frame(self.transcript_area, title="Conversación")
        input_frame = Frame(self.input_area, title="Mensaje")
        footer = Window(self.status_bar, height=1, style="class:status")
        return HSplit(
            [
                header_frame,
                top_row_container,
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

        @kb.add("tab")
        def _complete(_event) -> None:
            _event.app.current_buffer.start_completion(select_first=False)

        @kb.add("c-m")
        def _toggle_focus(_event) -> None:
            self.focus_chat = not self.focus_chat
            state = "enfoque chat" if self.focus_chat else "panel completo"
            self.status = f"Vista: {state}."
            self._refresh_ui()

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
        # Command prefixes: ":" and "/".
        # Use "//" to send text that starts with a slash.
        if prompt.startswith("//"):
            prompt = prompt[1:]
        elif prompt.startswith(":") or prompt.startswith("/"):
            command = prompt[1:].strip()
            if command:
                self.app.create_background_task(self._handle_command(command))
            return True
        self.app.create_background_task(self._handle_prompt(prompt))
        return True

    async def _handle_command(self, command: str) -> None:
        if command in {"q", "quit", "exit"}:
            self.app.exit()
            return
        if command == "help":
            self.status = "Comandos: /help /models /stream /focus /skills /skill <nombre>"
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
        if command == "focus":
            self.focus_chat = not self.focus_chat
            state = "enfoque chat" if self.focus_chat else "panel completo"
            self.status = f"Vista: {state}."
            self._refresh_ui()
            return
        if command == "skills":
            self._show_skills_status()
            self._refresh_ui()
            return
        if command.startswith("skill "):
            await self._handle_skill_command(command.split(None, 1)[1].strip())
            return
        self.status = f"Comando desconocido: :{command}"
        self._refresh_ui()

    async def _handle_skill_command(self, value: str) -> None:
        skill = value.lower().strip()
        if not skill:
            self.status = "Uso: :skill <nombre>"
            self._refresh_ui()
            return
        if skill in {"none", "off", "clear"}:
            self.active_skills = []
            self.status = "Habilidades desactivadas."
            self._refresh_ui()
            return
        if skill not in SKILL_PRESETS:
            self.status = f"Habilidad desconocida: {skill}. Usa :skills"
            self._refresh_ui()
            return
        if skill in self.active_skills:
            self.active_skills = [s for s in self.active_skills if s != skill]
            self.status = f"Habilidad desactivada: {skill}"
        else:
            self.active_skills.append(skill)
            self.status = f"Habilidad activada: {skill}"
        self._refresh_ui()

    def _show_skills_status(self) -> None:
        available = ", ".join(sorted(SKILL_PRESETS.keys()))
        active = ", ".join(self.active_skills) if self.active_skills else "ninguna"
        self.status = f"Skills activas: {active}. Disponibles: {available}"

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
        active_skills = ", ".join(self.active_skills) if self.active_skills else "ninguna"
        layout_mode = "enfoque chat" if self.focus_chat else "panel completo"
        self.summary_area.text = (
            f"Host: {self.config.ollama.host}\n"
            f"Modelo: {self.current_model}\n"
            f"Disponibles: {len(self.models)}\n"
            f"Streaming: {stream}\n"
            f"Habilidades: {active_skills}\n"
            f"Vista: {layout_mode}\n"
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
        for skill in self.active_skills:
            preset = SKILL_PRESETS.get(skill)
            if preset:
                messages.append({"role": "system", "content": f"[skill:{skill}] {preset}"})
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
