from flet import *
from flet import icons,colors
import appmenu
import section1
import sectioncomming

def main(page:Page):
	page.scroll=True
	page.add(
		appmenu.appmenu,
		section1.mysection1,
		sectioncomming.sectioncomming

		)

flet.app(target=main)
