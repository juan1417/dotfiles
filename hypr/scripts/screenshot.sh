#!/bin/bash
# Screenshot helper for Hyprland using grim + slurp + wl-copy

DIR="$HOME/Pictures/Screenshots"
mkdir -p "$DIR"

TIMESTAMP=$(date +%Y%m%d_%H%M%S)

case "$1" in
	screen)
		grim "$DIR/screenshot_$TIMESTAMP.png"
		grim - | wl-copy
		;;
	region)
		REGION=$(slurp)
		if [ -n "$REGION" ]; then
			grim -g "$REGION" "$DIR/screenshot_$TIMESTAMP.png"
			grim -g "$REGION" - | wl-copy
		fi
		;;
	window)
		ACTIVE=$(hyprctl activewindow -j)
		AT_X=$(echo "$ACTIVE" | jq -r '.at[0]')
		AT_Y=$(echo "$ACTIVE" | jq -r '.at[1]')
		SIZE_W=$(echo "$ACTIVE" | jq -r '.size[0]')
		SIZE_H=$(echo "$ACTIVE" | jq -r '.size[1]')
		grim -g "${AT_X},${AT_Y} ${SIZE_W}x${SIZE_H}" "$DIR/screenshot_$TIMESTAMP.png"
		grim -g "${AT_X},${AT_Y} ${SIZE_W}x${SIZE_H}" - | wl-copy
		;;
	*)
		echo "Uso: $0 {screen|region|window}"
		exit 1
		;;
esac
