from tkinter import *
from UI import UI
from Bowl import Bowl
<<<<<<< HEAD
from Fruit import Fruit
=======
from Score import Score
>>>>>>> c105617b8296f2b9d92f1c75c819887cb91a3452

class Game:


		
		

	def __init__(self):
		
		self.interface=UI(self)
		self.interface.displayMainMenu()
<<<<<<< HEAD
		self.interface.root.mainloop()



	def fruitFactory(self) : 
		print("132")
		self.listFruit.append(Fruit(self.interface.getMenu()))
		self.interface.getMenu().TkMenu.after(1000,self.fruitFactory())
		

	
	def play(self):
		print("Play !")
		self.inGame = True
		self.interface.hideMainMenu()
=======
		self.interface.root.TkMenu.mainloop()
		self.score=Score()
	def play(self):
		print("Play !")
>>>>>>> c105617b8296f2b9d92f1c75c819887cb91a3452
		self.interface.displayGameMenu()
		self.bowl=Bowl(self.interface.getMenu())
		self.interface.getMenu().TkMenu.bind('<KeyPress-Left>',lambda event :self.bowl.move("left"))
		self.interface.getMenu().TkMenu.bind('<KeyPress-Right>',lambda event :self.bowl.move("right"))
<<<<<<< HEAD
		self.listFruit=[]

=======

	def win(self):
		print("well play ! you won")
		self.interface.displayWinMenu()
>>>>>>> c105617b8296f2b9d92f1c75c819887cb91a3452

game=Game()




