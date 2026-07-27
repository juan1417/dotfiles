---------------
---- INPUT ----
---------------

hl.config({
	input = {
		kb_layout = "latam",
		kb_variant = "",
		kb_model = "",
		kb_options = "",
		kb_rules = "",

		follow_mouse = 1,

		sensitivity = 0,

		touchpad = {
			natural_scroll = true,
			tap_to_click = true,
			drag_lock = false,
			clickfinger_behavior = false,
			scroll_factor = 1.0,
			disable_while_typing = true,
			tap_and_drag = true,
		},
	},
})

hl.gesture({
	fingers = 3,
	direction = "horizontal",
	action = "workspace",
})

hl.device({
	name = "epic-mouse-v1",
	sensitivity = -0.5,
})
