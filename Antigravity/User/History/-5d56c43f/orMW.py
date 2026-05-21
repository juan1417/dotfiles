"""Configuration management for TermChat."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

import yaml

CONFIG_DIR = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config")) / "termchat"
DATA_DIR = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share")) / "termchat"
SKILLS_DIR = CONFIG_DIR / "skills"
PLUGINS_DIR = CONFIG_DIR / "plugins"
HISTORY_DIR = DATA_DIR / "history"

DEFAULT_CONFIG = {
    "model": "llama3.2",
    "ollama_url": "http://localhost:11434",
    "temperature": 0.7,
    "context_window": 4096,
    "system_prompt": "You are a helpful, concise assistant running inside a terminal. When creating skills, always output a complete Markdown skill file with YAML frontmatter and a Python execute() function.",
    "theme": "dark",
    "stream": True,
    "history_enabled": True,
    "max_history_sessions": 50,
    "context7_enabled": True,
    "context7_max_tokens": 8000,
}


@dataclass
class Config:
    model: str = "gemma2:2b"
    ollama_url: str = "http://localhost:11434"
    temperature: float = 0.7
    context_window: int = 4096
    system_prompt: str = DEFAULT_CONFIG["system_prompt"]
    theme: str = "dark"
    stream: bool = True
    history_enabled: bool = True
    max_history_sessions: int = 50
    context7_enabled: bool = True
    context7_max_tokens: int = 8000
    extra: dict = field(default_factory=dict)

    @classmethod
    def load(cls) -> "Config":
        """Load config from ~/.config/termchat/config.yaml, creating defaults if needed."""
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        SKILLS_DIR.mkdir(parents=True, exist_ok=True)
        PLUGINS_DIR.mkdir(parents=True, exist_ok=True)
        HISTORY_DIR.mkdir(parents=True, exist_ok=True)

        config_file = CONFIG_DIR / "config.yaml"
        if not config_file.exists():
            config_file.write_text(yaml.dump(DEFAULT_CONFIG, default_flow_style=False))

        raw = yaml.safe_load(config_file.read_text()) or {}
        return cls(
            model=raw.get("model", DEFAULT_CONFIG["model"]),
            ollama_url=raw.get("ollama_url", DEFAULT_CONFIG["ollama_url"]),
            temperature=raw.get("temperature", DEFAULT_CONFIG["temperature"]),
            context_window=raw.get("context_window", DEFAULT_CONFIG["context_window"]),
            system_prompt=raw.get("system_prompt", DEFAULT_CONFIG["system_prompt"]),
            theme=raw.get("theme", DEFAULT_CONFIG["theme"]),
            stream=raw.get("stream", DEFAULT_CONFIG["stream"]),
            history_enabled=raw.get("history_enabled", DEFAULT_CONFIG["history_enabled"]),
            max_history_sessions=raw.get("max_history_sessions", DEFAULT_CONFIG["max_history_sessions"]),
            context7_enabled=raw.get("context7_enabled", DEFAULT_CONFIG["context7_enabled"]),
            context7_max_tokens=raw.get("context7_max_tokens", DEFAULT_CONFIG["context7_max_tokens"]),
            extra=raw,
        )

    def save(self) -> None:
        """Persist current config to disk."""
        config_file = CONFIG_DIR / "config.yaml"
        data = {
            "model": self.model,
            "ollama_url": self.ollama_url,
            "temperature": self.temperature,
            "context_window": self.context_window,
            "system_prompt": self.system_prompt,
            "theme": self.theme,
            "stream": self.stream,
            "history_enabled": self.history_enabled,
            "max_history_sessions": self.max_history_sessions,
            "context7_enabled": self.context7_enabled,
            "context7_max_tokens": self.context7_max_tokens,
        }
        config_file.write_text(yaml.dump(data, default_flow_style=False))
