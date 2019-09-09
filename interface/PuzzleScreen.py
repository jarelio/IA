from kivy.uix.screenmanager import Screen
from kivy.animation import Animation

class PuzzleScreen(Screen):
	def __init__(self,**kwargs):

		super(PuzzleScreen,self).__init__(**kwargs)

	def verifyCollision(self,instance):
		blank = self.ids.blank

		x,y = instance.pos

		print(blank.pos)
		print(instance.pos)

		up = blank.collide_point(x+0.25,y)
		down = blank.collide_point(x-0.25,y)
		left = blank.collide_point(x,y-0.25)
		right = blank.collide_point(x,y+0.25)

		print(up,down,left,right)



	
	def buttonAction(self,instance):
		top_hint = instance.top_hint
		right_hint = instance.right_hint
		self.verifyCollision(instance)
		#animation = Animation(top_hint = top_hint-0.25) 
		#animation.start(instance) 

		