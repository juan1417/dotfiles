#!/usr/bin/env bash
set -euo pipefail

DOTFILES_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_DIR="${HOME}/.config"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

info()  { echo -e "${GREEN}[INFO]${NC} $1"; }
warn()  { echo -e "${YELLOW}[WARN]${NC} $1"; }
error() { echo -e "${RED}[ERROR]${NC} $1"; }

# Configs to sync (folder name -> optional target override)
declare -A CONFIGS=(
    ["alacritty"]="alacritty"
    ["hypr"]="hypr"
    ["nvim"]="nvim"
    ["fish"]="fish"
    ["waybar"]="waybar"
    ["rofi"]="rofi"
    ["mako"]="mako"
    ["btop"]="btop"
    ["micro"]="micro"
    ["opencode"]="opencode"
)

backup_and_link() {
    local src="$1"
    local dst="$2"

    if [ -d "$dst" ] && [ ! -L "$dst" ]; then
        local backup="${dst}.bak.$(date +%Y%m%d%H%M%S)"
        warn "Backing up existing $dst -> $backup"
        mv "$dst" "$backup"
    fi

    if [ -L "$dst" ]; then
        rm "$dst"
    fi

    ln -sf "$src" "$dst"
    info "Linked $src -> $dst"
}

copy_config() {
    local name="$1"
    local src="${DOTFILES_DIR}/${name}"
    local dst="${CONFIG_DIR}/${name}"

    if [ ! -d "$src" ]; then
        warn "Skipping ${name}: source not found"
        return
    fi

    if [ -d "$dst" ] && [ ! -L "$dst" ]; then
        local backup="${dst}.bak.$(date +%Y%m%d%H%M%S)"
        warn "Backing up existing ${name} -> ${backup}"
        cp -r "$dst" "$backup"
    fi

    mkdir -p "$dst"
    rsync -a --delete --exclude='.git' --exclude='node_modules' "$src/" "$dst/"
    info "Installed ${name}"
}

echo ""
echo "=============================="
echo "  Dotfiles Installer"
echo "=============================="
echo ""

# Sync configs
for name in "${!CONFIGS[@]}"; do
    copy_config "$name"
done

echo ""
info "Done! Restart your apps or log out/in for changes to take effect."
echo ""
