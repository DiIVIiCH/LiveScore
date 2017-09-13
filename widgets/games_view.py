import os

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from widgets.game_carousel import GameCarousel
from widgets.date_picker import DatePicker
from functools import partial
from datetime import datetime
from pytz import timezone, utc

root = os.path.split(__file__)[0]
root = root if root != '' else os.getcwd()
Builder.load_file('{}/kv/games_view.kv'.format(root))

class GamesView(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		car = GameCarousel()
		date = DatePicker()
		car.bind(current_slide = date.change_date)
		date.bind(date = car.date_picked)
		day = datetime.utcnow()
		date.date = utc.localize(day)	
		self.add_widget(car)
		self.add_widget(date)
		self.ids['carousel'] = car
