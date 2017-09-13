from kivy.properties import StringProperty
from kivy.lang import Builder
import os
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.properties import NumericProperty

root = os.path.split(__file__)[0]
root = root if root != '' else os.getcwd()
Builder.load_file('{}/kv/toast.kv'.format(root))


class Toast(Label):
	_transparency = NumericProperty(1.0)

	def __init__(self, text, *args, **kwargs):
		'''Show the toast in the main window.  The attatch_to logic from 
		:class:`~kivy.uix.modalview` isn't necessary because a toast really
		does need to go on top of everything.
		'''
		self.font_size=20
		self._bound = False
		self.color = [1,1,1,0]
		super(Toast, self).__init__(text=text, *args, **kwargs)

	def show(self):
		#duration = 5000 if length_long else 500
		#rampdown = duration * 0.1
		#if rampdown > 500:
		 #   rampdown = 500
		#if rampdown < 100:
		 #   rampdown = 100
		#self._rampdown = rampdown
		#self._duration = duration - rampdown
		Window.add_widget(self)
		#Clock.schedule_interval(self._in_out, 1/60.0)

	def close(self):
		Window.remove_widget(self)

	def on_texture_size(self, instance, size):
		self.size = list(map(lambda i: i * 2, size))
		if not self._bound:
			Window.bind(on_resize=self._align)
			self._bound = True
		self._align(None, Window.size)
            
	def _align(self, win, size):
		self.x = (size[0] - self.width) / 2.0
		self.y = size[1] * 0.1

	def _in_out(self, dt):
		self._duration -= dt * 1000
		if self._duration <= 0:
			self._transparency = 1.0 + (self._duration / self._rampdown)
		if -(self._duration) > self._rampdown:
			Window.remove_widget(self)
			return False

def toast(text):
	Toast(text=text).show()
