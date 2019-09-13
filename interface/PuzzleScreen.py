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
		self.values = [[1,2,3],[4,5,6],[7,8,0]]
		self.pos0 = (2,2)

		super(PuzzleScreen,self).__init__(**kwargs)

	def verifyCollision(self,instance,blank):
		pos = blank.pos
		x,y = instance.pos

		sides = {"up":[x,y+125],"down":[x,y-125],"left":[x-100,y],"right":[x+100,y]}
		for i in sides:
			if sides[i] == pos:
				x0,y0 = self.pos0
				if i == "up":
					self.values[y0][x0],self.values[y0+1][x0] = self.values[y0+1][x0],0
					self.pos0 = (x0,y0+1)
				elif i == "down":
					self.values[y0][x0],self.values[y0-1][x0] = self.values[y0-1][x0],0
					self.pos0 = (x0,y0-1)
				elif i == "left":
					self.values[y0][x0],self.values[y0][x0+1] = self.values[y0][x0+1],0
					self.pos0 = (x0+1,y0)
				else:
					self.values[y0][x0],self.values[y0][x0-1] = self.values[y0][x0-1],0
					self.pos0 = (x0-1,y0)

				self.steps.append((instance,i))
				return True
		return False

	def undo(self):
		blank = self.ids.blank
		x0,y0 = self.pos0
		try:
			instance,direction = self.steps.pop()

			if direction == "up":
				self.values[y0][x0],self.values[y0-1][x0] = self.values[y0-1][x0],0
				self.pos0 = (x0,y0-1)
			elif direction == "down":
				self.values[y0][x0],self.values[y0+1][x0] = self.values[y0+1][x0],0
				self.pos0 = (x0,y0+1)
			elif direction == "left":
				self.values[y0][x0],self.values[y0][x0-1] = self.values[y0][x0-1],0
				self.pos0 = (x0-1,y0)
			else:
				self.values[y0][x0],self.values[y0][x0+1] = self.values[y0][x0+1],0
				self.pos0 = (x0+1,y0)

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

	def __encontrarpeca0__(self):
		for i in range(3):
			for j in range(3):
				if (self.value[i][j] == 0):
					linha = i
					coluna = j
		return linha,coluna
				
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
			