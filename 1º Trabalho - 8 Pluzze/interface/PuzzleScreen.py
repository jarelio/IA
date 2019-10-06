from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.config import Config
import copy
import time
from Fila import Fila
from No import No
from Resolve import Resolve
from ia_oo import Runner

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '500')
Config.set('graphics', 'resizable', False)

class PuzzleScreen(Screen):
	def __init__(self,**kwargs):
		self.animationQueue = []
		self.steps =[]
		self.values = [[1,2,3],[4,5,6],[7,8,0]]
		self.pos0 = (2,2)

		super(PuzzleScreen,self).__init__(**kwargs)

		

	def verifyCollision(self,instance,blank):
		t,r = blank.pos_hint.values()
		top,right = instance.pos_hint.values()

		sides = {"up":[top+.25,right],"down":[top-.25,right],"left":[top,right-.25],"right":[top,right+.25]}
		for i in sides:
			if sides[i] == [t,r]:
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
		blank = self.ids["0"]
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

	def __encontrarpeca0__(self,value):
		for i in range(3):
			for j in range(3):
				if (value[i][j] == 0):
					linha = i
					coluna = j
		return linha,coluna

	def __disable__(self,instance,boolean,*args):
		instance.disabled = boolean
				
	def buttonAction(self,instance,*args):
		blank = self.ids["0"]
		x,y = instance.pos
		top_hint = instance.top_hint
		right_hint = instance.right_hint

		if self.verifyCollision(instance,blank):
			self.__swap__(instance,blank)
		else:
			anim = Animation(top_hint = top_hint+.01,duration = 0.05) + Animation(top_hint = top_hint, duration=0.05)+Animation(top_hint = top_hint-.01,duration = 0.05) + Animation(top_hint = top_hint, duration=0.05)
			anim.bind(on_start = lambda *args:self.__disable__(instance,True),on_complete = lambda *args:self.__disable__(instance,False))
			anim.start(instance)

	def __swap__(self,widget1,widget2):
		top1,top2 = widget1.top_hint,widget2.top_hint
		right1,right2 = widget1.right_hint,widget2.right_hint
		animation = Animation(top_hint = top2,right_hint = right2, duration = 0.1) 
		animation2 = Animation(top_hint = top1,right_hint = right1, duration = 0.1) 
		animation.start(widget1)
		animation2.start(widget2)
		self.__swapPos__(widget1,widget2)

	def __swapPos__(self,widget1,widget2):
		x1,y1 = widget1.pos
		x2,y2 = widget2.pos

		widget1.pos = (x2,y2)
		widget2.pos = (x1,y1)

	def run_animation(self,*args):
		if len(self.animationQueue)>0:
			a,w = self.animationQueue.pop(0)
			a.bind(on_complete = lambda *args:self.run_animation())
			a.start(w)

	def __swapThread__(self,widget1,widget2,pos1,pos2,*args):
		top1,top2 = pos1["top"],pos2["top"]
		right1,right2 = pos1["right"],pos2["right"]

		animation = Animation(top_hint = top2,right_hint = right2, duration = 0.1) 
		animation2 = Animation(top_hint = top1,right_hint = right1, duration = 0.1) 
	
		self.animationQueue.append((animation,widget1))
		self.animationQueue.append((animation2,widget2))

		self.dictPos[widget1.text]["pos"] = pos2
		self.dictPos["0"]["pos"] = pos1
		self.__swapPos__(widget1,widget2)
		


	def resolveBFS(self):
		bfsButton = self.ids["bfs"]
		bfsButton.disabled = True 

		self.dictPos = dict()

		for i in self.ids:
			wid = self.ids[i]
			if wid.text == '':
				self.dictPos["0"] = {"pos":wid.pos_hint}
			elif wid.text == "BFS" or wid.text == "A*":
				pass
			else:
				self.dictPos[wid.text] = {"pos":wid.pos_hint}

		
		meta = [[1,2,3],[4,5,6],[7,8,0]]
		
		no_inicial = No(self.values,None)
		#print(no_inicial.retornaValue())

		fila = Fila(no_inicial,[])
		#for i in fila.retornafila():
		#	print(i.retornaValue())
		

		resolve = Resolve(fila,no_inicial,meta).bfs()
		resolve.reverse()
		
		for no in resolve[1:]:
			blank = self.ids["0"]
			newValues = no.value

			linha,coluna = self.__encontrarpeca0__(newValues)
			self.pos0 = (linha,coluna)
			instance = self.ids[str(self.values[linha][coluna])]
			
			pos2 = copy.deepcopy(self.dictPos["0"]["pos"])
			pos1 = copy.deepcopy(self.dictPos[str(self.values[linha][coluna])]["pos"])

			anim = self.__swapThread__(instance,blank,pos1,pos2)
			
			self.values = newValues

		anim = Animation(disabled = False, duration = 0)
		self.animationQueue.append((anim,bfsButton))
		self.run_animation()

	def resolveA(self):
		aButton = self.ids["A"]
		aButton.disabled = True 

		self.dictPos = dict()
		for i in self.ids:
			wid = self.ids[i]
			if wid.text == '':
				self.dictPos["0"] = {"pos":wid.pos_hint}
			elif wid.text == "BFS" or wid.text == "A*":
				pass
			else:
				self.dictPos[wid.text] = {"pos":wid.pos_hint}


		solucao = Runner(5000,1,self.values).run().pop()

		for state in solucao[1:]:
			blank = self.ids["0"]
			newValues = state

			linha,coluna = self.__encontrarpeca0__(newValues)
			self.pos0 = (linha,coluna)
			instance = self.ids[str(self.values[linha][coluna])]
			
			pos2 = copy.deepcopy(self.dictPos["0"]["pos"])
			pos1 = copy.deepcopy(self.dictPos[str(self.values[linha][coluna])]["pos"])

			anim = self.__swapThread__(instance,blank,pos1,pos2)
			
			self.values = newValues

		anim = Animation(disabled = False, duration = 0)
		self.animationQueue.append((anim,aButton))
		self.run_animation()

