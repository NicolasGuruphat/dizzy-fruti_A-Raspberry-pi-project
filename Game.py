from tkinter import *
from UI import UI
from Bowl import Bowl
from Fruit import Fruit
from time import *
#from RaspberrySenseHat import RaspberrySenseHat
#from sense_hat import SenseHat         
class Game:

	def __init__(self):
		#self.sense = SenseHat()
		self.interface=UI(self)
		self.interface.displayMainMenu()
		self.listFruit=[]
		self.interface.root.TkMenu.mainloop()
		self.victory
		
	def fruitFactory(self) :
		if(not self.victory): 
			self.listFruit.append(Fruit(self.interface.getMenu()))
			if(not self.i<1000):
				self.i-=40
			self.interface.getMenu().TkMenu.after(self.i,self.fruitFactory)
			
	def fruitFalling(self) : 
		if(not self.victory):
			for fruit in self.listFruit :
				Fruit.moveDown(fruit,self.interface)
				if(Fruit.verifyCollisionBowl(fruit,self.bowl)):
					self.score+=fruit.point
					#self.SenseHat.add(fruit.color, fruit.point)
					self.listFruit.remove(fruit)
					self.victory=(self.score>=64)
				elif(Fruit.verifyCollisionGround(fruit,self.interface.menu.taille)):
					self.listFruit.remove(fruit)
					self.life-=1
					if(self.life==2):
						self.interface.getMenu().canvasVie1.configure(bg="white")
					elif(self.life==1):
						self.interface.getMenu().canvasVie2.configure(bg="white")

					print(self.life)
					if(self.life==0):
						self.loose()
			if(not self.victory):
				self.interface.getMenu().TkMenu.after(60,self.fruitFalling)
			else :
				self.win()

	def loop(self):
		orientation = self.sense.get_orientation()
		pitch = orientation['pitch']
		if pitch > 25 and pitch <=90:
			self.bowl.move("right")
		elif pitch<335 and pitch>270:
			self.bowl.move("left")
		self.interface.getMenu().TkMenu.after(5,self.loop)
 

	def play(self):
		print("Play !")
		self.i=2000
		self.life=3
		self.victory=False
		self.score=0
		#self.SenseHat = RaspberrySenseHat()
		self.interface.displayGameMenu()
		self.bowl=Bowl(self.interface.getMenu())
		self.interface.getMenu().TkMenu.bind('<KeyPress-Left>',lambda event :self.bowl.move("left"))
		self.interface.getMenu().TkMenu.bind('<KeyPress-Right>',lambda event :self.bowl.move("right"))
		self.fruitFactory()
		self.fruitFalling()
		#self.loop()

	def win(self):
		print("well play ! you won")
		self.interface.displayWinMenu()
	def loose(self):
		print("you loose")
		self.interface.displayLooseMenu()

game=Game()




