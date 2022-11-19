from flet import *
from flet import icons,colors
import json

base_url = "https://image.tmdb.org/t/p/original"
allmovie = Row(scroll=True)
s = []
with open('comming.json') as json_file:
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
                    weight="bold"),
                Text(f"Release Date : {x['release_date']}",
                    size=18,
                    color="red",
                    weight="bold"
                    )

                    ],alignment="center")
                )
            )
        )

sectioncomming = Container(
    bgcolor="black",
    width=500,
    height=500,

    border_radius = border_radius.only(topLeft=30,topRight=30),

    content=Column([
        Container(
            margin=10,
            content=Text("Comming soon",
                size=20,
                color="white",
                weight="bold"
                )

            ),
        allmovie

        ],spacing=0)

    )
