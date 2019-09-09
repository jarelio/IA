from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from PuzzleScreen import PuzzleScreen
from kivy.core.window import Window as w
w.clearcolor = (0,206,209, 0)

Builder.load_file('puzzleScreen.kv')

class puzzleApp(App):
	def build(self):
		return PuzzleScreen()

myApp = puzzleApp()

if __name__ == '__main__':
	myApp.run()
