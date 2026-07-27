#!/bin/bash

SHORTCUTS=(
    " Super+Q           Abrir terminal"
    " Super+R           Abrir launcher"
    " Super+E           File manager"
    " Super+C           Cerrar ventana"
    " Super+F           Pantalla completa"
    " Super+Shift+Space Cambiar layout"
    " Super+Alt+V       Toggle float"
    ""
    " --- NAVEGACION ---"
    " Super+h/j/k/l     Mover foco"
    " Super+Shift+h/j/k/l  Redimensionar"
    ""
    " --- WORKSPACES ---"
    " Super+1-3         Ir a workspace"
    " Super+Shift+1-3   Mover ventana"
    " Super+Scroll      Cambiar workspace"
    ""
    " --- SCRATCHPAD ---"
    " Super+T           Toggle scratchpad"
    " Super+Shift+T     Mover a scratchpad"
    ""
    " --- SCREENSHOTS ---"
    " Super+S           Screenshot pantalla"
    " Super+Shift+S     Screenshot region"
    " Super+Ctrl+S      Screenshot ventana"
    ""
    " --- CLIPBOARD ---"
    " Super+V           Historial clipboard"
    ""
    " --- SHORTCUTS ---"
    " Super+F1          Ver shortcuts"
)

printf '%s\n' "${SHORTCUTS[@]}" | rofi -dmenu -p "Shortcuts" \
    -theme-str "window { width: 500px; height: 500px; location: center; }" \
    -theme-str "listview { lines: 20; columns: 1; flow: vertical; }" \
    -theme-str "element { padding: 4px 8px; }" \
    -theme-str "element-text { font: 'IosevkaTerm Nerd Font 13'; expand: horizontal; }" \
    -theme-str "element selected { background-color: #CBA6F7; text-color: #1E1E2E; }"
