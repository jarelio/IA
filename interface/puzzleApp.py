from kivy.app import App
from kivy.lang import Builder
from Window import Window

Builder.load_file('window.kv')

class puzzleApp(App):
	def build(self):
		return Window()

myApp = puzzleApp()

if __name__ == '__main__':
	myApp.run()
