from kivy.uix.carousel import Carousel
from kivy.properties import StringProperty
from widgets.game_day import GameDay
from kivy.lang import Builder
import os
from kivy.uix.button import Button
from datetime import datetime, timedelta, date
from kivy.uix.carousel import Carousel
from kivy.app import App
from kivy.clock import Clock
from functools import partial
from kivy.properties import NumericProperty
import threading

#from kivy.config import Config


root = os.path.split(__file__)[0]
root = root if root != '' else os.getcwd()
Builder.load_file('{}/kv/game_carousel.kv'.format(root))

def set_direction(ind1, ind2):
	t1 = [(0,1),(1,2),(2,0)]
	t2 = [(2,1),(1,0),(0,2)]
	if (ind1,ind2) in t1:
		return 'r'
	elif (ind1,ind2) in t2:
		return 'l'
	else: return ''

class GameCarousel(Carousel):
	event = None
	prev_index = 0
	update_time = 0

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		for i in range(3):
			r = GameDay()
			self.add_widget(r)
		self.update_time = App.get_running_app().config.get('General','time')	


	def local_changed(self):
		for slide in self.slides:
			threading.Thread(target = partial(slide.update)).start()
			

	def time_changed(self, value):		
		self.update_time = value
		self.set_schedule()
	

	def date_picked(self, obj, value):
		if value != self.current_slide.date:			
			self.current_slide.date = value
			self.previous_slide.date = value - timedelta(days=1) 
			self.next_slide.date = value + timedelta(days=1)
			self.set_schedule()

	def on_index(self, *args):
		super().on_index(args)				
		self.set_schedule()
		delta = timedelta(days=1) 
		swipe_direction = set_direction(self.prev_index, self.index)
		if swipe_direction == 'l':
			self.previous_slide.data = []
			self.previous_slide.date = self.current_slide.date - delta
		elif swipe_direction == 'r':
			self.next_slide.data = []
			self.next_slide.date = self.current_slide.date + delta



	def on_touch_down(self, touch):
		self.prev_index = self.index
		super().on_touch_down(touch)

	   

	def set_schedule(self):
		Clock.unschedule(self.event)
		if int(self.update_time)>0:	
			self.event = Clock.schedule_interval(partial(self.current_slide.update, False),float(self.update_time))


