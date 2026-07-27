---------------------
---- KEYBINDINGS ----
---------------------

local programs = require("programs")

local mainMod = "SUPER"

-- Basics
hl.bind(mainMod .. " + Q", hl.dsp.exec_cmd(programs.terminal))
hl.bind(mainMod .. " + C", hl.dsp.window.close())
hl.bind(mainMod .. " + M", hl.dsp.exec_cmd("pkill Hyprland || hyprctl dispatch exit"))
hl.bind(mainMod .. " + E", hl.dsp.exec_cmd(programs.fileManager))
hl.bind(mainMod .. " + R", hl.dsp.exec_cmd(programs.menu))
hl.bind(mainMod .. " + F1", hl.dsp.exec_cmd("bash /home/juan/.config/waybar/scripts/shortcuts.sh"))
hl.bind(mainMod .. " + P", hl.dsp.window.pseudo())
hl.bind(mainMod .. " + SHIFT + SPACE", hl.dsp.layout("togglesplit"))
hl.bind(mainMod .. " + F", hl.dsp.window.fullscreen())

-- Float toggle (movido a Super+Alt+V)
hl.bind(mainMod .. " + ALT + V", hl.dsp.window.float({ action = "toggle" }))

-- Move focus (vim style)
hl.bind(mainMod .. " + h", hl.dsp.focus({ direction = "left" }))
hl.bind(mainMod .. " + l", hl.dsp.focus({ direction = "right" }))
hl.bind(mainMod .. " + k", hl.dsp.focus({ direction = "up" }))
hl.bind(mainMod .. " + j", hl.dsp.focus({ direction = "down" }))

-- Move focus (arrow keys)
hl.bind(mainMod .. " + left", hl.dsp.focus({ direction = "left" }))
hl.bind(mainMod .. " + right", hl.dsp.focus({ direction = "right" }))
hl.bind(mainMod .. " + up", hl.dsp.focus({ direction = "up" }))
hl.bind(mainMod .. " + down", hl.dsp.focus({ direction = "down" }))

-- Resize windows (vim style)
hl.bind(mainMod .. " + SHIFT + h", hl.dsp.window.resize({ x = -30, y = 0, relative = true }))
hl.bind(mainMod .. " + SHIFT + l", hl.dsp.window.resize({ x = 30, y = 0, relative = true }))
hl.bind(mainMod .. " + SHIFT + k", hl.dsp.window.resize({ x = 0, y = -30, relative = true }))
hl.bind(mainMod .. " + SHIFT + j", hl.dsp.window.resize({ x = 0, y = 30, relative = true }))

-- Workspaces
for i = 1, 10 do
	local key = i % 10
	hl.bind(mainMod .. " + " .. key, hl.dsp.focus({ workspace = i }))
	hl.bind(mainMod .. " + SHIFT + " .. key, hl.dsp.window.move({ workspace = i }))
end

-- Special workspace (scratchpad) - Super+T para evitar conflicto
hl.bind(mainMod .. " + T", hl.dsp.workspace.toggle_special("magic"))
hl.bind(mainMod .. " + SHIFT + T", hl.dsp.window.move({ workspace = "special:magic" }))

-- Scroll workspaces
hl.bind(mainMod .. " + mouse_down", hl.dsp.focus({ workspace = "e+1" }))
hl.bind(mainMod .. " + mouse_up", hl.dsp.focus({ workspace = "e-1" }))

-- Mouse move/resize
hl.bind(mainMod .. " + mouse:272", hl.dsp.window.drag(), { mouse = true })
hl.bind(mainMod .. " + mouse:273", hl.dsp.window.resize(), { mouse = true })

-----------------------
---- RESIZE SUBMAP ----
-----------------------

hl.bind(mainMod .. " + ALT + R", hl.dsp.submap("resize"))

hl.define_submap("resize", function()
	hl.bind("right", hl.dsp.window.resize({ x = 30, y = 0, relative = true }), { repeating = true })
	hl.bind("left", hl.dsp.window.resize({ x = -30, y = 0, relative = true }), { repeating = true })
	hl.bind("up", hl.dsp.window.resize({ x = 0, y = 30, relative = true }), { repeating = true })
	hl.bind("down", hl.dsp.window.resize({ x = 0, y = -30, relative = true }), { repeating = true })
	hl.bind("escape", hl.dsp.submap("reset"))
end)

-------------------------------
---- SCREENSHOTS (grim) ----
-------------------------------

hl.bind(mainMod .. " + S", hl.dsp.exec_cmd("$HOME/.config/hypr/scripts/screenshot.sh screen"))
hl.bind(mainMod .. " + SHIFT + S", hl.dsp.exec_cmd("$HOME/.config/hypr/scripts/screenshot.sh region"))
hl.bind(mainMod .. " + CTRL + S", hl.dsp.exec_cmd("$HOME/.config/hypr/scripts/screenshot.sh window"))

-------------------------------
---- CLIPBOARD (cliphist) ----
-------------------------------

hl.bind(mainMod .. " + V", hl.dsp.exec_cmd("cliphist list | wofi --dmenu | wl-copy"))

---------------------------
---- MULTIMEDIA KEYS ----
---------------------------

hl.bind("XF86AudioRaiseVolume", hl.dsp.exec_cmd("wpctl set-volume -l 1 @DEFAULT_AUDIO_SINK@ 5%+"), { locked = true, repeating = true })
hl.bind("XF86AudioLowerVolume", hl.dsp.exec_cmd("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-"), { locked = true, repeating = true })
hl.bind("XF86AudioMute", hl.dsp.exec_cmd("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"), { locked = true, repeating = true })
hl.bind("XF86AudioMicMute", hl.dsp.exec_cmd("wpctl set-mute @DEFAULT_AUDIO_SOURCE@ toggle"), { locked = true, repeating = true })

hl.bind("XF86MonBrightnessUp", hl.dsp.exec_cmd("brightnessctl -e4 -n2 set 5%+"), { locked = true, repeating = true })
hl.bind("XF86MonBrightnessDown", hl.dsp.exec_cmd("brightnessctl -e4 -n2 set 5%-"), { locked = true, repeating = true })

hl.bind("XF86AudioNext", hl.dsp.exec_cmd("playerctl next"), { locked = true })
hl.bind("XF86AudioPause", hl.dsp.exec_cmd("playerctl play-pause"), { locked = true })
hl.bind("XF86AudioPlay", hl.dsp.exec_cmd("playerctl play-pause"), { locked = true })
hl.bind("XF86AudioPrev", hl.dsp.exec_cmd("playerctl previous"), { locked = true })
