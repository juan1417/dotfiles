"""Rich-based TermChat UI with a polished dashboard layout."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass

from rich.align import Align
from rich.console import Console, Group, RenderableType
from rich.columns import Columns
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table
from rich.text import Text

from agent.config import AppConfig, load_config, save_config
from agent.ollama_client import ModelInfo, OllamaClient
from UI.models import ChatEntry


@dataclass(slots=True)
class RuntimeState:
    status: str = "Listo. Escribe un mensaje para empezar."
    busy: bool = False


class RichTermChat:
    """Terminal UI rendered with Rich."""

    def __init__(self, config: AppConfig | None = None) -> None:
        self.config = config or load_config()
        self.client = OllamaClient(self.config)
        self.console = Console()
        self.entries: list[ChatEntry] = []
        self.models: list[ModelInfo] = []
        self.current_model = self.config.ollama.model
        self.state = RuntimeState()

    async def run(self) -> None:
        try:
            await self._refresh_models()
            self._render()
            await self._main_loop()
        except KeyboardInterrupt:
            self.console.print("\n[bold yellow]TermChat cerrado.[/bold yellow]")

    async def _main_loop(self) -> None:
        while True:
            self._render()
            try:
                user_input = self.console.input("[bold cyan]› [/bold cyan]")
            except EOFError:
                break

            prompt = user_input.strip()
            if not prompt:
                continue

            if prompt.startswith(":"):
                handled = await self._handle_command(prompt[1:].strip())
                if handled:
                    continue

            self.entries.append(ChatEntry(role="user", content=prompt))
            self.entries.append(ChatEntry(role="assistant", content=""))
            self.state.busy = True
            self.state.status = "Consultando Ollama..."
            self._render()

            try:
                answer = await self._process_message()
                self.entries[-1] = ChatEntry(role="assistant", content=answer)
                self.state.status = "Respuesta recibida."
            except Exception as exc:
                if self.entries and self.entries[-1].role == "assistant" and not self.entries[-1].content:
                    self.entries.pop()
                self.state.status = f"Error: {exc}"
                self.console.print(f"[bold red]Error:[/bold red] {exc}")
            finally:
                self.state.busy = False

    async def _handle_command(self, command: str) -> bool:
        if command in {"q", "quit", "exit"}:
            raise KeyboardInterrupt
        if command == "help":
            self._show_help()
            return True
        if command == "models":
            await self._refresh_models()
            self.state.status = f"{len(self.models)} modelo(s) disponibles."
            return True
        if command.startswith("color "):
            color = command.split(None, 1)[1].strip()
            self.config.ui.panel_color = color
            try:
                save_config(self.config)
            except Exception:
                pass
            self.state.status = f"Color guardado: {color}"
            return True
        if command.startswith("opacity "):
            try:
                value = int(command.split(None, 1)[1].strip())
                value = max(0, min(100, value))
                self.config.ui.panel_opacity = value
                try:
                    save_config(self.config)
                except Exception:
                    pass
                self.state.status = f"Opacidad guardada: {value}%"
            except Exception:
                self.state.status = "Opacidad inválida (0-100)."
            return True
        if command == "stream":
            self.config.ollama.stream = not self.config.ollama.stream
            self.state.status = f"Streaming {'on' if self.config.ollama.stream else 'off'}"
            return True
        self.state.status = f"Comando desconocido: :{command}"
        return True

    async def _process_message(self) -> str:
        history = self._build_messages()
        if self.config.ollama.stream:
            return await self._stream_response(history)
        return await self.client.complete(history, model=self.current_model)

    async def _stream_response(self, history: list[dict[str, str]]) -> str:
        tokens: list[str] = []
        async for chunk in self.client.stream_chat(history, model=self.current_model):
            tokens.append(chunk)
            self.entries[-1] = ChatEntry(role="assistant", content="".join(tokens))
            self.state.status = "Recibiendo streaming..."
            self._render()
        return "".join(tokens)

    async def _refresh_models(self) -> None:
        try:
            self.models = await self.client.list_models()
            available = {model.name for model in self.models}
            if self.models and self.current_model not in available:
                self.current_model = self.models[0].name
        except Exception as exc:
            self.models = []
            self.state.status = f"No se pudo consultar Ollama: {exc}"

    def _render(self) -> None:
        self.console.clear()
        self.console.print(self._build_dashboard())

    def _build_dashboard(self) -> RenderableType:
        return Group(
            self._build_header(),
            self._build_summary_row(),
            self._build_body(),
            self._build_footer(),
        )

    def _build_header(self) -> RenderableType:
        title = Text()
        title.append("TermChat", style="bold white")
        title.append("  ", style="white")
        title.append("Local Ollama assistant", style="bold cyan")

        subtitle = Text()
        subtitle.append("Modelo activo: ", style="dim")
        subtitle.append(self.current_model or "-", style="bold green")
        subtitle.append("   ", style="dim")
        subtitle.append("Stream: ", style="dim")
        subtitle.append("on" if self.config.ollama.stream else "off", style="bold yellow")

        return Panel(
            Group(title, subtitle),
            border_style="cyan",
            title="TermChat",
            subtitle=self.config.ollama.host,
            padding=(1, 2),
        )

    def _build_summary_row(self) -> RenderableType:
        model_panel = Panel(
            self._build_model_card(),
            border_style="green",
            title="Estado",
            padding=(0, 1),
        )
        status_panel = Panel(
            self._build_status_card(),
            border_style="magenta",
            title="Sesión",
            padding=(0, 1),
        )
        help_panel = Panel(
            self._build_help_preview(),
            border_style="yellow",
            title="Comandos",
            padding=(0, 1),
        )
        return Columns([model_panel, status_panel, help_panel], equal=True, expand=True)

    def _build_model_card(self) -> RenderableType:
        table = Table.grid(padding=(0, 1))
        table.add_column(style="cyan", no_wrap=True)
        table.add_column(style="white")
        table.add_row("Host", self.config.ollama.host)
        table.add_row("Modelo", self.current_model or "-")
        table.add_row("Disponibles", str(len(self.models)))
        table.add_row("Streaming", "on" if self.config.ollama.stream else "off")
        return table

    def _build_status_card(self) -> RenderableType:
        table = Table.grid(padding=(0, 1))
        table.add_column(style="cyan", no_wrap=True)
        table.add_column(style="white")
        table.add_row("Mensajes", str(len(self.entries)))
        table.add_row("Historial", str(self.config.history_limit))
        table.add_row("Estado", "Procesando" if self.state.busy else "Listo")
        return table

    def _build_help_preview(self) -> RenderableType:
        lines = Text()
        lines.append(":help", style="bold")
        lines.append(" ayuda\n", style="white")
        lines.append(":models", style="bold")
        lines.append(" lista modelos\n", style="white")
        lines.append(":stream", style="bold")
        lines.append(" toggle stream\n", style="white")
        lines.append(":color #RRGGBB", style="bold")
        lines.append(" guardar color\n", style="white")
        lines.append(":opacity N", style="bold")
        lines.append(" guardar opacidad", style="white")
        return lines

    def _build_body(self) -> RenderableType:
        transcript = self._build_transcript()
        model_sidebar = self._build_sidebar()
        return Columns(
            [
                Panel(transcript, border_style="blue", title="Conversación", padding=(1, 2), expand=True),
                Panel(model_sidebar, border_style="bright_black", title="Modelos", padding=(1, 1), width=32),
            ],
            expand=True,
            equal=False,
        )

    def _build_transcript(self) -> RenderableType:
        if not self.entries:
            return Align.center(Text("La conversación todavía está vacía.", style="dim"), vertical="middle")

        blocks: list[RenderableType] = []
        for entry in self.entries[-self.config.history_limit :]:
            blocks.append(self._render_entry(entry))
        return Group(*blocks)

    def _render_entry(self, entry: ChatEntry) -> RenderableType:
        role_style = "bold green" if entry.role == "user" else "bold blue"
        content = entry.content.strip() or "..."
        body = Text(content)
        return Panel(
            Group(Text(entry.role.upper(), style=role_style), body),
            border_style="green" if entry.role == "user" else "blue",
            padding=(0, 1),
        )

    def _build_sidebar(self) -> RenderableType:
        table = Table.grid(padding=(0, 1))
        table.add_column(style="cyan", no_wrap=True)
        table.add_column(style="white")
        if not self.models:
            table.add_row("Modelos", "No disponibles")
        else:
            for model in self.models[:12]:
                size_mb = model.size / (1024**2) if getattr(model, "size", 0) else 0
                table.add_row(model.name, f"{size_mb:.1f} MB")
        return table

    def _build_footer(self) -> RenderableType:
        status = Text()
        status.append("Estado: ", style="bold cyan")
        status.append(self.state.status, style="white")

        hint = Text()
        hint.append("Escribe tu mensaje y Enter. ", style="dim")
        hint.append("Ctrl+C", style="bold")
        hint.append(" para salir.", style="dim")

        return Panel(
            Group(status, Rule(style="bright_black"), hint),
            border_style="bright_black",
            padding=(0, 1),
        )

    def _show_help(self) -> None:
        self.console.print(
            Panel(
                Group(
                    Text("Comandos disponibles", style="bold yellow"),
                    Text(
                        ":help - ayuda\n"
                        ":models - recargar y listar modelos\n"
                        ":stream - alternar streaming\n"
                        ":color #RRGGBB - guardar color preferido\n"
                        ":opacity N - guardar opacidad\n"
                        ":quit - salir",
                    ),
                ),
                border_style="yellow",
                title="Ayuda",
                padding=(1, 2),
            )
        )

    def _build_messages(self) -> list[dict[str, str]]:
        messages: list[dict[str, str]] = [{"role": "system", "content": self.config.assistant.system_prompt}]
        for entry in self.entries[-self.config.history_limit :]:
            if entry.content:
                messages.append({"role": entry.role, "content": entry.content})
        return messages


async def run() -> None:
    app = RichTermChat()
    await app.run()


if __name__ == "__main__":
    asyncio.run(run())
