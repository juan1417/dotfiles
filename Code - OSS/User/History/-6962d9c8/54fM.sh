#!/bin/bash

# Script de arranque para TermChat

# Obtener el directorio del script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Entrar al directorio del proyecto
cd "$SCRIPT_DIR" || exit

# Activar el entorno virtual si existe
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Ejecutar la aplicación
python main.py
