import os

from kivy.uix.recycleview import RecycleView
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from datetime import datetime, time, date
from widgets.game_layout import GameLayout
import threading  
from params import *
import requests
from kivy.core.window import Window
from widgets.toast import Toast
from kivy.app import App
from pytz import timezone
from tzlocal import get_localzone
from functools import partial

root = os.path.split(__file__)[0]
root = root if root != '' else os.getcwd()
Builder.load_file('{}/kv/game_day.kv'.format(root))



class GameDay(RecycleView):
	_date = ObjectProperty(datetime(year = 1970, month = 1, day = 1))
	error = StringProperty()

	def get_date(self):
		return self._date

	def set_date(self, value):
		
		if isinstance(value, date):
			value = datetime.combine(value, datetime.min.time())
		eastern = timezone('US/Eastern')
		value = eastern.localize(value)
		self._date = value
		self.data = []
		threading.Thread(target = self.load_gameday).start()

	date = property(get_date, set_date)

	def load_gameday(self):
		view, data = self.get_day_schedule()
		self.data = []
		self.viewclass = view 
		self.data = data
		for w in Window.children:
				if isinstance(w, Toast):
					w.close()
					break
	
	def get_day_schedule(self):
		url = base_url+datetime.strftime(self.date,'%m/%d/%Y')+'&LeagueID='+leagueID+'&DayOffset='+dayOffset		
		data = []
		try: 
			req = requests.get(url, headers = headers)
			response = req.json()
			games = response['resultSets'][0]['rowSet']
			linescore = response['resultSets'][1]['rowSet']
			team_id=0
			self.error = ''
			if games:
				linescore = self.right_team_order(games, linescore)
				viewclass = 'GameLayout'
				for game in games:
					d={}
					d['homeTeam'] = teams[game[HOME_TEAM_ID]] if game[HOME_TEAM_ID] in teams.keys() else linescore[team_id+1][TEAM_CITY_NAME]
					d['visitorTeam'] = teams[game[VISITOR_TEAM_ID]] if game[VISITOR_TEAM_ID] in teams.keys() else linescore[team_id][TEAM_CITY_NAME]
					d['status'] = self.check_time(game[GAME_STATUS_TEXT].upper())
					d['homeScore'] = linescore[team_id+1][PTS] if linescore[team_id+1][PTS] is not None else 0
					d['visitorScore'] = linescore[team_id][PTS] if linescore[team_id][PTS] is not None else 0
					team_id+=2
					data.append(d)				
			else:
				viewclass = 'Label'
				data=[{'text':'NO GAMES THIS DAY', 'color':(0,0,0,1), 'font_size':'25sp'}]
				self.error = 'No'
		except requests.ConnectionError:
			viewclass = 'Label'
			data=[{'text':'CONNECTION ERROR', 'color':(0,0,0,1), 'font_size':'25sp'}]
			self.error = 'Con'
		return viewclass, data

	def update(self, tap = False, dt=0):
		if tap:
			Toast('UPDATE', color=[1,1,1,1]).show()
		if self.error == 'Con':
			self.load_gameday()
		elif self.error == '':
			view, data = self.get_day_schedule()
			if view == 'GameLayout':
				for k,game in enumerate(self.data):
					game['homeScore'] = data[k]['homeScore']
					game['status'] = data[k]['status']
					game['visitorScore'] = data[k]['visitorScore']
				self.refresh_from_data()
			else:
				self.viewclass = view 
				self.data = data
		for w in Window.children:
				if isinstance(w, Toast):
					w.close()
					break


	def check_time(self, time_str):
		if 'ET' in time_str and int(App.get_running_app().config.get('General','local')):
			game_time = datetime.strptime(time_str[:-3], '%I:%M %p')
			local_tz = get_localzone()		
			game_date = self.date	
			game_date = game_date.replace(hour = game_time.hour, minute = game_time.minute)		
			game_date = game_date.astimezone(local_tz)	
			return game_date.strftime('%H:%M %m/%d/%y')
		else:
			return time_str

	def on_touch_down(self, touch):
		super(GameDay, self).on_touch_down(touch)		   
		if touch.is_double_tap:
			threading.Thread(target = partial(self.update, True)).start()
		self._touch = touch
		return True

	def right_team_order(self, games, linescore):
		team_id = 0
		for game in games:
			
			if game[HOME_TEAM_ID] != linescore[team_id+1][LINESCORE_TEAM_ID]:
				
				linescore[team_id+1], linescore[team_id] = linescore[team_id], linescore[team_id+1]
				
			team_id+=2
		return linescore
