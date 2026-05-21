"""Rich-based TUI for TermChat — simple, clean, no transparency issues."""

from __future__ import annotations

import asyncio
import sys
from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text
from rich.table import Table

from agent.config import AppConfig, load_config, save_config
from agent.ollama_client import OllamaClient, ModelInfo
from UI.widgets import ChatEntry


class RichTermChat:
    """Terminal UI using Rich — no Textual, clean rendering."""

    def __init__(self, config: AppConfig | None = None) -> None:
        self.config = config or load_config()
        self.client = OllamaClient(self.config)
        self.console = Console()
        self.entries: list[ChatEntry] = []
        self.models: list[ModelInfo] = []
        self.current_model = self.config.ollama.model
        self._active_task: asyncio.Task[None] | None = None

    async def run(self) -> None:
        """Main event loop."""
        try:
            await self._refresh_models()
            self._show_welcome()
            await self._main_loop()
        except KeyboardInterrupt:
            self.console.print("[yellow]Interrumpido por el usuario.[/yellow]")
        except Exception as exc:
            self.console.print(f"[red]Error fatal: {exc}[/red]")

    def _show_welcome(self) -> None:
        """Display welcome screen."""
        self.console.clear()
        self.console.print("[bold cyan]╔══════════════════════════════════╗[/bold cyan]")
        self.console.print("[bold cyan]║         TermChat - Ollama        ║[/bold cyan]")
        self.console.print("[bold cyan]╚══════════════════════════════════╝[/bold cyan]")
        self.console.print()
        self.console.print(
            f"[blue]Modelo:[/blue] {self.current_model}\n"
            f"[blue]Host:[/blue] {self.config.ollama.host}\n"
            f"[blue]Streaming:[/blue] {'on' if self.config.ollama.stream else 'off'}\n"
            f"[blue]Modelos disponibles:[/blue] {len(self.models)}"
        )
        self.console.print("\n[yellow]Comandos:[/yellow]")
        self.console.print(":help — muestra esta ayuda")
        self.console.print(":color #RRGGBB — no hace nada (Rich no tiene fondos)")
        self.console.print("Ctrl+Q — salir")
        self.console.print()

    async def _main_loop(self) -> None:
        """Read user input and process commands."""
        while True:
            self._refresh_screen()
            prompt_text = "[cyan]> [/cyan]"
            try:
                user_input = self.console.input(prompt_text)
            except EOFError:
                break

            user_input = user_input.strip()
            if not user_input:
                continue

            # Quick commands
            if user_input.startswith(":"):
                cmd = user_input[1:].strip()
                if cmd == "quit" or cmd == "q":
                    break
                elif cmd == "help":
                    self._show_help()
                elif cmd.startswith("color "):
                    color = cmd.split(None, 1)[1].strip()
                    self.config.ui.panel_color = color
                    try:
                        save_config(self.config)
                    except Exception:
                        pass
                    self.console.print(f"[green]✓ Color guardado: {color}[/green]")
                elif cmd.startswith("opacity "):
                    try:
                        val = int(cmd.split(None, 1)[1].strip())
                        val = max(0, min(100, val))
                        self.config.ui.panel_opacity = val
                        try:
                            save_config(self.config)
                        except Exception:
                            pass
                        self.console.print(f"[green]✓ Opacidad: {val}%[/green]")
                    except Exception:
                        self.console.print("[red]✗ Opacidad inválida (0-100)[/red]")
                elif cmd == "models":
                    await self._refresh_models()
                    self._show_models()
                else:
                    self.console.print(f"[red]Comando desconocido: :{cmd}[/red]")
                continue

            # Regular message
            self.entries.append(ChatEntry(role="user", content=user_input))
            self.entries.append(ChatEntry(role="assistant", content=""))
            self._refresh_screen()
            self.console.print("[yellow]⟳ Consultando Ollama...[/yellow]")

            try:
                await self._process_message()
            except Exception as exc:
                if self.entries and self.entries[-1].role == "assistant" and not self.entries[-1].content:
                    self.entries.pop()
                self.console.print(f"[red]✗ Error: {exc}[/red]")

    async def _process_message(self) -> None:
        """Send message to Ollama and get response."""
        history = self._build_messages()
        try:
            if self.config.ollama.stream:
                answer = await self._stream_response(history)
            else:
                answer = await self.client.complete(history, model=self.current_model)
            self.entries[-1] = ChatEntry(role="assistant", content=answer)
        except Exception:
            raise

    async def _stream_response(self, history: list[dict[str, str]]) -> str:
        """Stream response from Ollama."""
        tokens: list[str] = []
        async for chunk in self.client.stream_chat(history, model=self.current_model):
            tokens.append(chunk)
            self.entries[-1] = ChatEntry(role="assistant", content="".join(tokens))
            # Print token without newline for live feedback
            self.console.print(chunk, end="", highlight=False)
        self.console.print()  # newline after stream
        return "".join(tokens)

    async def _refresh_models(self) -> None:
        """Fetch available models from Ollama."""
        try:
            self.models = await self.client.list_models()
            if self.models and self.current_model not in {m.name for m in self.models}:
                self.current_model = self.models[0].name
        except Exception as exc:
            self.console.print(f"[red]Error al consultar modelos: {exc}[/red]")

    def _refresh_screen(self) -> None:
        """Redraw the screen."""
        self.console.clear()
        self._show_header()
        self._show_transcript()

    def _show_header(self) -> None:
        """Show header with app title and status."""
        header_text = (
            f"[bold cyan]TermChat[/bold cyan] | "
            f"[blue]Modelo:[/blue] {self.current_model} | "
            f"[blue]Stream:[/blue] {'on' if self.config.ollama.stream else 'off'}"
        )
        self.console.print(Panel(header_text, style="cyan", expand=False))

    def _show_transcript(self) -> None:
        """Show conversation history."""
        if not self.entries:
            self.console.print("[dim]La conversación todavía está vacía.[/dim]")
            return

        for entry in self.entries:
            role_style = "bold green" if entry.role == "user" else "bold blue"
            role_text = Text(f"{entry.role.upper()}:", style=role_style)
            self.console.print(role_text)
            content_lines = entry.content.strip().split("\n")
            for line in content_lines:
                self.console.print(f"  {line}")
            self.console.print()

    def _show_help(self) -> None:
        """Show help message."""
        self.console.print(
            Panel(
                "[bold]Comandos disponibles:[/bold]\n"
                ":help — muestra esta ayuda\n"
                ":models — lista modelos disponibles\n"
                ":color #RRGGBB — guarda color preferido (visual)\n"
                ":opacity N — guarda opacidad (0-100)\n"
                ":quit — salir",
                title="Ayuda",
                style="yellow",
            )
        )

    def _show_models(self) -> None:
        """Display available models in a table."""
        if not self.models:
            self.console.print("[red]No hay modelos disponibles.[/red]")
            return

        table = Table(title="Modelos disponibles", style="cyan")
        table.add_column("Nombre", style="green")
        table.add_column("Tamaño", justify="right")

        for model in self.models:
            size_mb = model.size / (1024**2) if hasattr(model, "size") else 0
            table.add_row(model.name, f"{size_mb:.1f} MB")

        self.console.print(table)

    def _build_messages(self) -> list[dict[str, str]]:
        """Build message history for Ollama."""
        messages: list[dict[str, str]] = [{"role": "system", "content": self.config.assistant.system_prompt}]
        for entry in self.entries[-self.config.history_limit :]:
            if entry.content:
                messages.append({"role": entry.role, "content": entry.content})
        return messages


async def run() -> None:
    """Main entry point."""
    app = RichTermChat()
    await app.run()


if __name__ == "__main__":
    asyncio.run(run())
