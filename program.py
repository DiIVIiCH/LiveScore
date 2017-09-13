from kivy.app import App
from widgets.main_view import MainView
from libs.kivymd.theming import ThemeManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty
from settings_json import settings_json
from widgets.settings_view import LiveScoreSettings


class LiveScore(App):
	theme_cls = ThemeManager()

	def build(self):
		self.settings_cls = LiveScoreSettings
		self.use_kivy_settings = False
		main_w = MainView(self.create_settings())
		return main_w	

	def build_config(self, config):
		config.setdefaults('General', {'local': 0,'time': 0})

	def build_settings(self, settings):
		settings.add_json_panel('Settings', self.config, data=settings_json)

	def on_config_change(self, config, section, key, value):
		if section == 'General' and key == 'local':
			self.root.ids.gamesview.ids.carousel.local_changed()
		elif section == 'General' and key == 'time':
			self.root.ids.gamesview.ids.carousel.time_changed(value)

