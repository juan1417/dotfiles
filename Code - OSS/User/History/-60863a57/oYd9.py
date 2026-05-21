"""Data models for TermChat — independent of UI framework."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ChatEntry:
    """A single message in the conversation."""
    role: str
    content: str
