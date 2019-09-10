from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '500')
Config.set('graphics', 'resizable', False)

class PuzzleScreen(Screen):
	def __init__(self,**kwargs):

		super(PuzzleScreen,self).__init__(**kwargs)

	def verifyCollision(self,instance,blank):
		pos = blank.pos
		x,y = instance.pos

		sides = {"up":[x,y+125],"down":[x,y-125],"left":[x-100,y],"right":[x+100,y]}
		for i in sides.values():
			if i == pos:
				return True
		return False



	
	def buttonAction(self,instance):
		blank = self.ids.blank
		

		if self.verifyCollision(instance,blank):
			top_hint = instance.top_hint
			right_hint = instance.right_hint
			top_hintB = blank.top_hint
			right_hintB = blank.right_hint
			animation = Animation(top_hint = top_hintB,right_hint = right_hintB, duration = 0.5) 
			animation2 = Animation(top_hint = top_hint,right_hint = right_hint, duration = 0.5) 
			animation.start(instance) 
			animation2.start(blank)

		