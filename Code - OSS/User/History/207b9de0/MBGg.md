## TermChat

TermChat is a local terminal assistant built on Ollama and a custom TUI.

### Run

```bash
uv sync
uv run termchat
```

### Configuration

The app reads configuration from `config/termchat.toml` in the repository and from `~/.config/termchat/config.toml` in the user profile.

Main settings:

- `ollama.host`: Ollama HTTP endpoint, usually `http://localhost:11434`
- `ollama.model`: default model name
- `ollama.stream`: enables streaming responses
- `ui.panel_opacity`: visual opacity used by the translucent panel
- `assistant.system_prompt`: base system prompt for the local assistant

### Notes

The first TUI version uses transparent and semi-transparent panels to reduce background occlusion, but actual transparency still depends on the terminal emulator.
