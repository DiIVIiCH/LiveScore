from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
import os
from kivy.lang import Builder
from pathlib import Path

root = os.path.split(__file__)[0]
root = root if root != '' else os.getcwd()
Builder.load_file('{}/kv/game_layout.kv'.format(root))
home_dir = os.path.dirname(root)
default_path = '{}/data/logos/{}.png'.format( home_dir,'default')

class GameLayout(BoxLayout):
	visitorTeam = StringProperty('1')
	homeTeam = StringProperty('2')
	status = StringProperty('FINAL')
	homeScore = NumericProperty(0)
	visitorScore = NumericProperty(0)
	text_color = ObjectProperty([0, 0, 0, 1])
	homeLogo = StringProperty(default_path)
	visitorLogo = StringProperty(default_path)

	def check_path(self, value):
		s = '{}/data/logos/{}.png'.format( home_dir,value.lower())
		if Path(s).is_file():
			return s
		else:
			return default_path

	def on_visitorTeam(self, instance, value):		
		self.visitorLogo = self.check_path(value)


	def on_homeTeam(self, instance, value):
		self.homeLogo = self.check_path(value)

	

class TeamLogo(Label):
	source = StringProperty()