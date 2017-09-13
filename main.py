from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')

from program import LiveScore



def main():
	app = LiveScore()
	app.run()

	
if __name__ in ('__main__', '__android__'):
	main()