from __future__ import annotations

from dataclasses import dataclass

from textual.widgets import Input, Static


@dataclass(slots=True)
class ChatEntry:
    role: str
    content: str


def format_transcript(entries: list[ChatEntry]) -> str:
    if not entries:
        return "La conversación todavía está vacía."

    parts: list[str] = []
    for entry in entries:
        role = entry.role.upper()
        header = f"{role}:"
        body = entry.content.strip() or "..."
        parts.append(f"{header}\n{body}")
    return "\n\n".join(parts)


class TranscriptView(Static):
    def set_entries(self, entries: list[ChatEntry]) -> None:
        self.update(format_transcript(entries))


class PromptInput(Input):
    def __init__(self) -> None:
        super().__init__(placeholder="Escribe tu mensaje y presiona Enter", id="prompt")


class ModelSummary(Static):
    def set_state(self, model: str, host: str, stream: bool, available: int) -> None:
        stream_label = "on" if stream else "off"
        self.update(f"Model: {model}   Host: {host}   Stream: {stream_label}   Available: {available}")


class StatusLine(Static):
    def set_message(self, message: str) -> None:
        self.update(message)
