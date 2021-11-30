from tkinter import *
from UI import UI
from Bowl import Bowl
from Fruit import Fruit
from Score import Score

class Game:



	def __init__(self):
		
		self.interface=UI(self)
		self.interface.displayMainMenu()
		self.interface.root.mainloop()



	def fruitFactory(self) : 
		print("132")
		self.listFruit.append(Fruit(self.interface.getMenu()))
		self.interface.getMenu().TkMenu.after(1000,self.fruitFactory())
		

	
	def play(self):
		print("Play !")
		self.interface.hideMainMenu()
        self.interface.displayGameMenu()
        self.bowl=Bowl(self.interface.getMenu())
		self.interface.getMenu().TkMenu.bind('<KeyPress-Left>',lambda event :self.bowl.move("left"))
		self.interface.getMenu().TkMenu.bind('<KeyPress-Right>',lambda event :self.bowl.move("right"))
		self.listFruit=[]
		self.interface.root.TkMenu.mainloop()
		self.score=Score()


	def win(self):
		print("well play ! you won")
		self.interface.displayWinMenu()

game=Game()




