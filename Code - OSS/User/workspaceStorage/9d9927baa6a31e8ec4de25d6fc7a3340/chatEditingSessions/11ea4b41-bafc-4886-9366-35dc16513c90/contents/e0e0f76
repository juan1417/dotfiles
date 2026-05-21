from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import os
import tomllib
from typing import Any


def _default_ollama_host() -> str:
    return os.environ.get("OLLAMA_HOST", "http://localhost:11434")


def _default_model() -> str:
    return os.environ.get("OLLAMA_MODEL", "llama3.1")


@dataclass(slots=True)
class OllamaConfig:
    host: str = field(default_factory=_default_ollama_host)
    model: str = field(default_factory=_default_model)
    stream: bool = True


@dataclass(slots=True)
class UIConfig:
    panel_opacity: int = 24
    panel_color: str = "#0f172a"
    accent: str = "#7aa2f7"
    transparent_background: bool = True


@dataclass(slots=True)
class AssistantConfig:
    system_prompt: str = (
        "You are TermChat, a concise local terminal assistant. "
        "Prioritize actionable responses, short explanations, and safe defaults."
    )
    mode: str = "default"
    skills: list[str] = field(default_factory=list)
    rules: list[str] = field(default_factory=list)
    context_files: list[str] = field(default_factory=list)


@dataclass(slots=True)
class AppConfig:
    ollama: OllamaConfig = field(default_factory=OllamaConfig)
    ui: UIConfig = field(default_factory=UIConfig)
    assistant: AssistantConfig = field(default_factory=AssistantConfig)
    history_limit: int = 24

    @classmethod
    def load(cls, path: Path | None = None) -> "AppConfig":
        config = cls()
        for candidate in _config_candidates(path):
            if candidate.exists():
                data = tomllib.loads(candidate.read_text(encoding="utf-8"))
                config.apply(data)
        return config

    def apply(self, data: dict[str, Any]) -> None:
        ollama = data.get("ollama", {})
        if isinstance(ollama, dict):
            self.ollama.host = str(ollama.get("host", self.ollama.host))
            self.ollama.model = str(ollama.get("model", self.ollama.model))
            self.ollama.stream = bool(ollama.get("stream", self.ollama.stream))

        ui = data.get("ui", {})
        if isinstance(ui, dict):
            self.ui.panel_opacity = int(ui.get("panel_opacity", self.ui.panel_opacity))
            self.ui.accent = str(ui.get("accent", self.ui.accent))
            self.ui.transparent_background = bool(ui.get("transparent_background", self.ui.transparent_background))

        assistant = data.get("assistant", {})
        if isinstance(assistant, dict):
            self.assistant.system_prompt = str(assistant.get("system_prompt", self.assistant.system_prompt))
            self.assistant.mode = str(assistant.get("mode", self.assistant.mode))
            self.assistant.skills = _normalize_list(assistant.get("skills", self.assistant.skills))
            self.assistant.rules = _normalize_list(assistant.get("rules", self.assistant.rules))
            self.assistant.context_files = _normalize_list(assistant.get("context_files", self.assistant.context_files))

        if "history_limit" in data:
            self.history_limit = int(data["history_limit"])


def load_config(path: Path | None = None) -> AppConfig:
    return AppConfig.load(path)


def _write_toml(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(data, encoding="utf-8")


def _ui_toml_snippet(ui: UIConfig) -> str:
    return ("[ui]\n"
            f'panel_opacity = {ui.panel_opacity}\n'
            f'panel_color = "{ui.panel_color}"\n'
            f'accent = "{ui.accent}"\n'
            f'transparent_background = {"true" if ui.transparent_background else "false"}\n')


def _default_config_path() -> Path:
    repo_root = Path(__file__).resolve().parents[2]
    return repo_root / "config" / "termchat.toml"


def _persist_ui_config(ui: UIConfig, path: Path | None = None) -> None:
    target = path or _default_config_path()
    # Write a minimal toml containing just the UI section to avoid clobbering other settings.
    _write_toml(target, _ui_toml_snippet(ui))


def save_config(app_config: AppConfig, path: Path | None = None) -> None:
    """Persist UI-related settings to a simple TOML file (repo config by default)."""
    _persist_ui_config(app_config.ui, path)


def _config_candidates(path: Path | None) -> list[Path]:
    if path is not None:
        return [path]

    repo_root = Path(__file__).resolve().parents[2]
    user_config = Path.home() / ".config" / "termchat" / "config.toml"
    return [repo_root / "config" / "termchat.toml", user_config]


def _normalize_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    if isinstance(value, tuple):
        return [str(item) for item in value]
    return [str(value)]
