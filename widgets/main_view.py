from libs.kivymd.navigationdrawer import NavigationLayout
from widgets.nav_drawer import NavDrawer
from widgets.games_view import GamesView
class MainView(NavigationLayout):
	def __init__(self, settings, **kwargs):
		super().__init__(**kwargs)
		nav = NavDrawer()
		nav.add_widget(settings)
		self.add_widget(nav)
		gv = GamesView()
		self.add_widget(gv)
		self.ids['gamesview'] = gv
