#!/bin/bash
# Bluetooth menu script for Waybar using bluetoothctl + wofi

action=$(echo -e "Power On\nPower Off\nScan Devices\nPair Device\nConnect Device\nDisconnect Device" | \
    wofi --dmenu -p "Bluetooth" -W 300 -H 250 2>/dev/null)

case "$action" in
    "Power On")
        bluetoothctl power on 2>/dev/null && \
            notify-send "Bluetooth" "Encendido" -t 2000
        ;;
    "Power Off")
        bluetoothctl power off 2>/dev/null && \
            notify-send "Bluetooth" "Apagado" -t 2000
        ;;
    "Scan Devices")
        bluetoothctl -- scan on &
        sleep 3
        bluetoothctl -- scan off
        devices=$(bluetoothctl devices 2>/dev/null | \
            awk '{print $2 " " substr($0, index($0,$3))}' | \
            wofi --dmenu -p "Devices" -W 400 -H 350 2>/dev/null)
        if [ -n "$devices" ]; then
            mac=$(echo "$devices" | awk '{print $1}')
            bluetoothctl pair "$mac" 2>/dev/null && \
                notify-send "Bluetooth" "Emparejado con $mac" -t 2000 || \
                notify-send "Bluetooth" "Error al emparejar" -t 2000
        fi
        ;;
    "Connect Device")
        devices=$(bluetoothctl devices 2>/dev/null | \
            awk '{print $2 " " substr($0, index($0,$3))}' | \
            wofi --dmenu -p "Select Device" -W 400 -H 350 2>/dev/null)
        if [ -n "$devices" ]; then
            mac=$(echo "$devices" | awk '{print $1}')
            bluetoothctl connect "$mac" 2>/dev/null && \
                notify-send "Bluetooth" "Conectado a $mac" -t 2000 || \
                notify-send "Bluetooth" "Error al conectar" -t 2000
        fi
        ;;
    "Disconnect Device")
        devices=$(bluetoothctl info 2>/dev/null | grep "Connected: yes" -B 2 | \
            awk '/Device/ {print $2}' | \
            wofi --dmenu -p "Disconnect" -W 300 -H 200 2>/dev/null)
        if [ -n "$devices" ]; then
            bluetoothctl disconnect "$devices" 2>/dev/null && \
                notify-send "Bluetooth" "Desconectado" -t 2000
        fi
        ;;
esac
