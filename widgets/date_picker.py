import os
from datetime import datetime, timedelta, date
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.date_picker import MDDatePicker
from datetime import datetime, timedelta, date
from kivy.properties import ObjectProperty
from widgets.toast import Toast

root = os.path.split(__file__)[0]
root = root if root != '' else os.getcwd()
Builder.load_file('{}/kv/date_picker.kv'.format(root))

class DatePicker(BoxLayout):
	date = ObjectProperty(date(year = 1970, month = 1, day = 1))

	def on_date(self, instance, value):
		self.set_text()

	def set_date(self, value):		
		self.date = value
		Toast('LOADING', color=[1,1,1,1]).show()

	def change_date(self, obj, value):
		self.date = value.date

	def set_text(self):
		self.ids.date_button.text = datetime.strftime(self.date,'%m/%d/%Y')

	def show_date_picker(self):
		MDDatePicker(self.set_date,self.date.year, self.date.month, self.date.day).open()
	
