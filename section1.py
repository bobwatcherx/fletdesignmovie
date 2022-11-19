from flet import *
from flet import icons,colors
import json

base_url = "https://image.tmdb.org/t/p/original"
# FOR DETAILS READ DOCS TMDB
allmovie = Row(scroll=True)
s = []
with open('data.json') as json_file:
    data = json.load(json_file)
    s = data['results']


# NOW PUSH TO NEW WIDGET
for x in s:
	allmovie.controls.append(
		Card(
			elevation=30,
			content=Container(
			width=160,
			height=330,
			padding=10,
			border = border.symmetric(vertical=border.BorderSide(5,"orange")),
			border_radius = border_radius.all(30),
			bgcolor="white",		
				content=Column([
					Image(
				src=base_url+x["poster_path"],
				height=200,
				border_radius = border_radius.all(30),
				fit="contain"
					),
				Text(x['original_title'],
					size=18,
					weight="bold")

					],alignment="center")
				)
			)
		)


mysection1 = Column([
	Text("Trending",size=20,weight="bold"),

	allmovie,

	])
