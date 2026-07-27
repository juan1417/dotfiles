#!/bin/bash
STATUS=$(playerctl status 2>/dev/null)
if [ "$STATUS" = "Playing" ]; then
    echo -e "\u23F8"
elif [ "$STATUS" = "Paused" ]; then
    echo -e "\u25B6"
else
    echo -e "\u25B6"
fi
