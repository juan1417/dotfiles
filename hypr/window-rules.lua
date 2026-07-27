--------------------------------
---- WINDOWS AND WORKSPACES ----
--------------------------------

-- Persistent workspaces (always show 3 dots)
hl.workspace_rule({ workspace = "1", persistent = true })
hl.workspace_rule({ workspace = "2", persistent = true })
hl.workspace_rule({ workspace = "3", persistent = true })

-- Ignore maximize requests
hl.window_rule({
	name = "suppress-maximize-events",
	match = { class = ".*" },
	suppress_event = "maximize",
})

-- Fix dragging issues with XWayland
hl.window_rule({
	name = "fix-xwayland-drags",
	match = {
		class = "^$",
		title = "^$",
		xwayland = true,
		float = true,
		fullscreen = false,
		pin = false,
	},
	no_focus = true,
})

-- Hyprland-run windowrule
hl.window_rule({
	name = "move-hyprland-run",
	match = { class = "hyprland-run" },
	move = "20 monitor_h-120",
	float = true,
})

-- wifipy: open in a floating window
hl.window_rule({
	name = "wifipy-float",
	match = { title = "wifipy" },
	float = true,
	size = "700 550",
	center = true,
})

-- calendarpy: open in a floating window
hl.window_rule({
	name = "calendarpy-float",
	match = { title = "calendarpy" },
	float = true,
	size = "700 550",
	center = true,
})

-- pavucontrol: floating
hl.window_rule({
	name = "pavucontrol-float",
	match = { class = "pavucontrol" },
	float = true,
	size = "500 400",
	center = true,
})
