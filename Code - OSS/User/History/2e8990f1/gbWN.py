from __future__ import annotations

import asyncio

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container
from textual.widgets import Input, Static

from agent.config import AppConfig, load_config
from agent.ollama_client import ModelInfo, OllamaClient
from UI.widgets import ChatEntry, ModelSummary, PromptInput, StatusLine, TranscriptView


class TermChatApp(App[None]):
    TITLE = "TermChat"
    SUB_TITLE = "Local Ollama assistant"
    CSS = """
    Screen {
        background: transparent;
    }

    #shell {
        width: 100%;
        height: 100%;
        padding: 1 2;
        background: transparent;
    }

    #panel {
        width: 100%;
        height: 100%;
        layout: vertical;
        padding: 1 2;
        border: round #7aa2f7;
        background: #0f172a 24%;
    }

    #title {
        height: auto;
        text-style: bold;
        color: #e2e8f0;
        margin-bottom: 1;
    }

    #model_summary {
        height: auto;
        color: #93c5fd;
        margin-bottom: 1;
    }

    #transcript {
        height: 1fr;
        border: round #334155;
        background: transparent;
        padding: 1 1;
        scrollbar-background: transparent;
    }

    #prompt {
        margin-top: 1;
    }

    #status {
        height: auto;
        color: #94a3b8;
        margin-top: 1;
    }
    """
    BINDINGS = [
        Binding("ctrl+q", "quit", "Quit"),
        Binding("ctrl+r", "reload_models", "Reload models"),
        Binding("ctrl+s", "toggle_stream", "Toggle stream"),
        Binding("f2", "cycle_model", "Next model"),
        Binding("ctrl+t", "toggle_transparency", "Toggle transparency"),
    ]

    def __init__(self, config: AppConfig | None = None) -> None:
        super().__init__()
        self.config = config or load_config()
        self.client = OllamaClient(self.config)
        self.entries: list[ChatEntry] = []
        self.models: list[ModelInfo] = []
        self.current_model = self.config.ollama.model
        self._active_task: asyncio.Task[None] | None = None
        # runtime flag for transparency
        self._transparency_enabled = bool(self.config.ui.transparent_background)

    def compose(self) -> ComposeResult:
        with Container(id="shell"):
            with Container(id="panel"):
                yield Static("TermChat", id="title")
                yield ModelSummary(id="model_summary")
                yield TranscriptView(id="transcript")
                yield PromptInput()
                yield StatusLine(id="status")

    async def on_mount(self) -> None:
        panel = self.query_one("#panel")
        # Honor the user's transparency preference. True transparency depends on the terminal emulator.
        if self._transparency_enabled:
            panel.styles.background = "transparent"
            try:
                self.styles.background = "transparent"
            except Exception:
                pass
        else:
            color = getattr(self.config.ui, "panel_color", "#0f172a")
            panel.styles.background = f"{color} {self.config.ui.panel_opacity}%"
        # Ensure inner widgets do not force an opaque background
        try:
            self.query_one(TranscriptView).styles.background = "transparent"
        except Exception:
            pass
        try:
            self.query_one(PromptInput).styles.background = "transparent"
        except Exception:
            pass
        try:
            self.query_one(ModelSummary).styles.background = "transparent"
        except Exception:
            pass
        try:
            self.query_one(StatusLine).styles.background = "transparent"
        except Exception:
            pass

        await self._refresh_models()
        self._refresh_views("Listo. Escribe un mensaje para empezar.")
        # focus the prompt input widget
        try:
            self.query_one(PromptInput).focus()
        except Exception:
            pass

    def action_toggle_transparency(self) -> None:
        """Toggle transparent background vs colored panel at runtime."""
        panel = self.query_one("#panel")
        self._transparency_enabled = not self._transparency_enabled
        if self._transparency_enabled:
            panel.styles.background = "transparent"
            try:
                self.styles.background = "transparent"
            except Exception:
                pass
            # make inner widgets transparent as well
            for w in (TranscriptView, PromptInput, ModelSummary, StatusLine):
                try:
                    self.query_one(w).styles.background = "transparent"
                except Exception:
                    pass
            self._set_status("Fondo: transparente")
        else:
            color = getattr(self.config.ui, "panel_color", "#0f172a")
            panel.styles.background = f"{color} {self.config.ui.panel_opacity}%"
            # keep inner widgets transparent to avoid full opaque blocks; borders remain
            for w in (TranscriptView, PromptInput, ModelSummary, StatusLine):
                try:
                    self.query_one(w).styles.background = "transparent"
                except Exception:
                    pass
            self._set_status("Fondo: color semitransparente")

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.input.id != "prompt":
            return

        prompt = event.value.strip()
        if not prompt:
            return

        event.input.value = ""
        self.entries.append(ChatEntry(role="user", content=prompt))
        self.entries.append(ChatEntry(role="assistant", content=""))
        self._refresh_views("Consultando Ollama...")

        if self._active_task and not self._active_task.done():
            self._active_task.cancel()

        self._active_task = asyncio.create_task(self._handle_prompt())

    async def _handle_prompt(self) -> None:
        history = self._build_messages()
        try:
            if self.config.ollama.stream:
                answer = await self._stream_response(history)
            else:
                answer = await self.client.complete(history, model=self.current_model)

            self.entries[-1] = ChatEntry(role="assistant", content=answer)
            self._refresh_views("Respuesta recibida.")
        except asyncio.CancelledError:
            self._set_status("Solicitud cancelada.")
            raise
        except Exception as exc:
            if self.entries and self.entries[-1].role == "assistant" and not self.entries[-1].content:
                self.entries.pop()
            self._set_status(f"Error de Ollama: {exc}")
            self.notify(str(exc), severity="error")
        finally:
            self._active_task = None

    async def _stream_response(self, history: list[dict[str, str]]) -> str:
        tokens: list[str] = []
        async for chunk in self.client.stream_chat(history, model=self.current_model):
            tokens.append(chunk)
            self.entries[-1] = ChatEntry(role="assistant", content="".join(tokens))
            self._refresh_views("Recibiendo streaming...")
        return "".join(tokens)

    async def _refresh_models(self) -> None:
        try:
            self.models = await self.client.list_models()
            if self.models and self.current_model not in {model.name for model in self.models}:
                self.current_model = self.models[0].name
            self._set_status(f"{len(self.models)} modelo(s) disponibles en Ollama.")
        except Exception as exc:
            self.models = []
            self._set_status(f"No se pudo consultar Ollama: {exc}")

    def action_reload_models(self) -> None:
        asyncio.create_task(self._refresh_models())

    def action_toggle_stream(self) -> None:
        self.config.ollama.stream = not self.config.ollama.stream
        mode = "activado" if self.config.ollama.stream else "desactivado"
        self._set_status(f"Streaming {mode}.")

    def action_cycle_model(self) -> None:
        if not self.models:
            self._set_status("No hay modelos cargados.")
            return

        names = [model.name for model in self.models]
        if self.current_model not in names:
            self.current_model = names[0]
        else:
            index = names.index(self.current_model)
            self.current_model = names[(index + 1) % len(names)]
        self._refresh_views(f"Modelo activo: {self.current_model}")

    def _build_messages(self) -> list[dict[str, str]]:
        messages: list[dict[str, str]] = [{"role": "system", "content": self.config.assistant.system_prompt}]
        for entry in self.entries[-self.config.history_limit :]:
            if entry.content:
                messages.append({"role": entry.role, "content": entry.content})
        return messages

    def _refresh_views(self, status: str) -> None:
        self.query_one(TranscriptView).set_entries(self.entries)
        self.query_one(ModelSummary).set_state(
            model=self.current_model,
            host=self.config.ollama.host,
            stream=self.config.ollama.stream,
            available=len(self.models),
        )
        self._set_status(status)

    def _set_status(self, message: str) -> None:
        self.query_one(StatusLine).set_message(message)


def run() -> None:
    TermChatApp().run()
