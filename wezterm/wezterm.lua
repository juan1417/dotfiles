local wezterm = require("wezterm")
local config = {}

-- ═══════════════════════════════════════════════════════════
-- FUENTE Y LIGATURAS (Aquí es donde WezTerm gana)
-- ═══════════════════════════════════════════════════════════
config.font = wezterm.font("Iosevka Custom")
config.font_size = 14.0

-- Activar ligaturas explícitamente
config.harfbuzz_features = { "liga", "calt" }

-- ═══════════════════════════════════════════════════════════
-- COLORES (Catppuccin Mocha + Tu acento Naranja)
-- ═══════════════════════════════════════════════════════════
config.color_scheme = "Catppuccin Mocha"

-- Personalización de colores (Cursor naranja, selección)
config.colors = {
	cursor_bg = "#ff6b35", -- Tu naranja
	cursor_fg = "#1e1e2e", -- Fondo oscuro
	cursor_border = "#ff6b35",

	selection_fg = "#1e1e2e",
	selection_bg = "#f5e0dc",

	-- Tab bar minimalista
	tab_bar = {
		background = "#1e1e2e",
		active_tab = { bg_color = "#ff6b35", fg_color = "#1e1e2e" },
		inactive_tab = { bg_color = "#313244", fg_color = "#cdd6f4" },
	},
}

-- ═══════════════════════════════════════════════════════════
-- VENTANA Y COMPORTAMIENTO
-- ═══════════════════════════════════════════════════════════
config.window_decorations = "NONE" -- Hyprland pone los bordes
config.window_background_opacity = 0.90
config.window_padding = { left = 10, right = 10, top = 10, bottom = 10 }

-- ═══════════════════════════════════════════════════════════
-- SHELL (Fish)
-- ═══════════════════════════════════════════════════════════
config.default_prog = { "/usr/bin/fish" }

-- ═══════════════════════════════════════════════════════════
-- ATAJOS DE TECLADO (Estándar + Wayland)
-- ═══════════════════════════════════════════════════════════
config.keys = {
	{ key = "c", mods = "CTRL|SHIFT", action = wezterm.action({ CopyTo = "ClipboardAndPrimarySelection" }) },
	{ key = "v", mods = "CTRL|SHIFT", action = wezterm.action({ PasteFrom = "Clipboard" }) },
}
-- ═══════════════════════════════════════════════════════════
-- PESTAÑAS (Opcional: Ocultar si prefieres usar solo Hyprland)
-- ═══════════════════════════════════════════════════════════
config.enable_tab_bar = true
config.hide_tab_bar_if_only_one_tab = true -- Se oculta si solo hay 1 pestaña

return config
