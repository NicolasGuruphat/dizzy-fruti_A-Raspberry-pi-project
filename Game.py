from tkinter import *
from UI import UI
from Bowl import Bowl
from Fruit import Fruit
from Score import Score
import threading
from time import *
from random import randint

class Game:

	def __init__(self):
		self.interface=UI(self)
		self.interface.displayMainMenu()
		self.listFruit=[]
		self.interface.root.TkMenu.mainloop()

	def fruitFactory(self) : 
		self.listFruit.append(Fruit(self.interface.getMenu()))
		self.interface.getMenu().TkMenu.after(1000,self.fruitFactory)
			
	def fruitFalling(self) : 
		for i in  range (len(self.listFruit)) :
			Fruit.moveDown(self.listFruit[i],self.interface)
		self.interface.getMenu().TkMenu.after(60,self.fruitFalling)

	def play(self):
		print("Play !")
		self.interface.displayGameMenu()
		self.bowl=Bowl(self.interface.getMenu())
		self.interface.getMenu().TkMenu.bind('<KeyPress-Left>',lambda event :self.bowl.move("left"))
		self.interface.getMenu().TkMenu.bind('<KeyPress-Right>',lambda event :self.bowl.move("right"))
		self.score=Score()
		self.fruitFactory()
		self.fruitFalling()
	

	def win(self):
		print("well play ! you won")
		self.interface.displayWinMenu()




game=Game()




