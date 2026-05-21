#!/usr/bin/env bash
# Script de Screenshots para Hyprland

# Directorio para guardar
DIR="$HOME/Pictures/Screenshots"
mkdir -p "$DIR"

# Nombre del archivo con fecha
FILE="screenshot_$(date +%Y-%m-%d_%H-%M-%S).png"

# Función para notificar
notify() {
    notify-send "📸 Captura guardada" "$DIR/$FILE" -i camera-photo
}

case "$1" in
    # Pantalla completa
    full)
        grim "$DIR/$FILE"
        notify
        ;;
    # Ventana activa
    active)
        # Obtiene las coordenadas de la ventana activa
        GEOM=$(hyprctl activewindow | grep at: | head -n 1 | awk '{print $2}' | sed 's/,//')
        SIZE=$(hyprctl activewindow | grep size: | head -n 1 | awk '{print $2}' | sed 's/,//')
        grim -g "$GEOM,$SIZE" "$DIR/$FILE"
        notify
        ;;
    # Selección de zona
    area)
        grim -g "$(slurp)" "$DIR/$FILE"
        notify
        ;;
    # Editar inmediatamente con Satty (Recomendado)
    edit)
        grim -g "$(slurp)" - | satty -f - -o "$DIR/$FILE"
        notify
        ;;
esac
