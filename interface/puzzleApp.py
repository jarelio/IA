from kivy.app import App
from kivy.lang import Builder
from PuzzleScreen import PuzzleScreen
from kivy.core.window import Window as w
w.clearcolor = (0.1,0.1,0.1, 0)

Builder.load_file('puzzleScreen.kv')

class puzzleApp(App):
	def build(self):
		return PuzzleScreen()

myApp = puzzleApp()

if __name__ == '__main__':
	myApp.run()
