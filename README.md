# Dotfiles

Personal configuration files for Arch Linux / CachyOS with Hyprland (Wayland).

## What's included

| App | Config path | Description |
|---|---|---|
| **Alacritty** | `alacritty/` | GPU-accelerated terminal (TOML config) |
| **Hyprland** | `hypr/` | Wayland compositor (Lua config) |
| **Neovim** | `nvim/` | LazyVim-based editor config |
| **Fish** | `fish/` | Shell config, completions, functions |
| **Waybar** | `waybar/` | Status bar with custom scripts |
| **Rofi** | `rofi/` | Application launcher |
| **Mako** | `mako/` | Notification daemon |
| **Btop** | `btop/` | System monitor |
| **Micro** | `micro/` | Terminal editor with Catppuccin themes |
| **OpenCode** | `opencode/` | AI coding assistant config & agents |

## Quick install

```bash
git clone https://github.com/juan1417/dotfiles.git ~/dotfiles
cd ~/dotfiles
chmod +x install.sh
./install.sh
```

## Manual install

Copy each directory to `~/.config/`:

```bash
# Example: Alacritty
cp -r alacritty/ ~/.config/alacritty/

# Example: Hyprland
cp -r hypr/ ~/.config/hypr/
```

## Requirements

- **Compositor**: Hyprland
- **Terminal**: Alacritty
- **Shell**: Fish
- **Editor**: Neovim (LazyVim)
- **Bar**: Waybar
- **Launcher**: Rofi
- **Notifications**: Mako
- **System monitor**: Btop

## Screenshot

<!-- Add screenshot here -->

## License

Personal use.
