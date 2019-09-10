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
		self.steps =[]
		super(PuzzleScreen,self).__init__(**kwargs)

	def verifyCollision(self,instance,blank):
		pos = blank.pos
		x,y = instance.pos

		sides = {"up":[x,y+125],"down":[x,y-125],"left":[x-100,y],"right":[x+100,y]}
		for i in sides.values():
			if i == pos:
				self.steps.append(instance)
				return True
		return False

	def undo(self):
		blank = self.ids.blank
		try:
			instance = self.steps.pop()
			top_hint = instance.top_hint
			right_hint = instance.right_hint
			top_hintB = blank.top_hint
			right_hintB = blank.right_hint
			animation = Animation(top_hint = top_hintB,right_hint = right_hintB, duration = 0.1) 
			animation2 = Animation(top_hint = top_hint,right_hint = right_hint, duration = 0.1) 
			animation.start(instance) 
			animation2.start(blank)
		except Exception as e:
			pass
				
	
	def buttonAction(self,instance):
		blank = self.ids.blank
		x,y = instance.pos
		top_hint = instance.top_hint
		right_hint = instance.right_hint

		if self.verifyCollision(instance,blank):
			
			top_hintB = blank.top_hint
			right_hintB = blank.right_hint
			animation = Animation(top_hint = top_hintB,right_hint = right_hintB, duration = 0.1) 
			animation2 = Animation(top_hint = top_hint,right_hint = right_hint, duration = 0.1) 
			animation.start(instance) 
			animation2.start(blank)
		else:
			anim = Animation(top_hint = top_hint+.01,duration = 0.05) + Animation(top_hint = top_hint, duration=0.05)+Animation(top_hint = top_hint-.01,duration = 0.05) + Animation(top_hint = top_hint, duration=0.05)
			anim.start(instance)
			