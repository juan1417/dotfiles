## Plan: TUI para asistente local (TermChat)

TL;DR: Crear una librería TUI mínima y un wrapper para Ollama, integrar la TUI con los componentes básicos (vista de chat, caja de entrada, selector de modelo) y arrancar la app desde `main.py`. Recomiendo usar `textual` por su soporte async y widgets modernos; alternativa: `prompt_toolkit` para menor peso.

**Steps**
1. Diseñar wrapper de Ollama: implementar `agent/ollama_client.py` con funciones `list_models()`, `generate(prompt, stream=False)` y soporte sync/async (priorizar async si usamos `textual`).
2. Añadir gestión de configuración: `agent/config.py` que cargue JSON/TOML desde `~/.config/termchat/config.toml` (model por defecto, rutas, modo streaming).
3. Implementar TUI principal: `UI/tui_app.py` (basado en `textual.App`) que arranque la interfaz y gestione eventos de teclado y tareas de streaming.
4. Crear componentes: `UI/components/chat_view.py`, `UI/components/input_box.py`, `UI/components/model_selector.py`.
5. Integrar con entrypoint: actualizar [main.py](main.py) para lanzar la TUI y documentar pasos en [README.md](README.md).
6. Añadir/actualizar dependencias en `pyproject.toml` si se confirma `textual` o `prompt_toolkit`.

**Relevant files**
- [UI/app.py](UI/app.py) — implementación actual de `TermChat` que sirve como referencia de renderizado.
- [UI/widget.py](UI/widget.py) — clase `Widget` simple; útil como fallback para render no-TTY.
- [main.py](main.py) — punto de entrada a actualizar para arrancar la TUI.
- [pyproject.toml](pyproject.toml) — contiene dependencia `ollama`; actualizará con dependencias TUI.
- [README.md](README.md) — documentar instalación y uso.
- agent/config/ — carpeta existente para persistir configuración y modos.

**Verification**
1. Unit tests básicos para `agent/ollama_client.py` (mockear SDK `ollama`): `list_models()` y `generate()`.
2. Ejecutar la app localmente: `python main.py` abre la TUI y permite enviar un prompt y recibir respuesta (no streaming inicial).
3. Prueba de streaming: enviar prompt largo y verificar que el `chat_view` se actualiza en tiempo real.

**Decisions**
- Librería TUI recomendada: `textual` (soporta async/streaming, ya aparece en el entorno). Se mitiga el problema de fondo usando `background: transparent` y paneles semitransparentes, pero la transparencia total depende del terminal. Alternativa: `prompt_toolkit` si prefieres evitar cualquier dependencia visual del emulador.
- Cliente Ollama: preferible asíncrono si adoptamos `textual` para evitar bloqueos UI.
- Config storage: archivo TOML en `~/.config/termchat/config.toml` (más portable que usar solo env vars).

**Further Considerations**
1. ¿Deseas que implemente el esqueleto inicial (archivos `agent/ollama_client.py`, `UI/tui_app.py`, y actualizar `main.py`) usando `textual`? Si no, elige `prompt_toolkit`.
2. ¿Prefieres streaming por defecto o como opción configurable? (recomendado: configurable `stream=false|true`).
