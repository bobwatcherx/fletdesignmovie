from flet import *
from flet import icons,colors


appmenu = AppBar(
	bgcolor="black",
	center_title=True,
	leading=IconButton(
		icon=icons.MENU,
		icon_color="white",
		icon_size=30
		),
	title=Text("Movie`X",
		size=30,
		color="white",
		weight="bold"
		),
	actions=[
		IconButton(
		icon=icons.SEARCH,
		icon_color="white",
		icon_size=30
		),

	]

	)
