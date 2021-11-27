from tkinter import *
from UI import UI
from Bowl import Bowl

class Game:

	def __init__(self):
		self.interface=UI(self)
		self.interface.displayMainMenu()
		self.interface.root.mainloop()
		
	
	def play(self):
		print("Play !")
		self.interface.hideMainMenu()
		self.interface.displayGameMenu()
		self.bowl=Bowl(self.interface.getMenu())
		self.interface.getMenu().TkMenu.bind('<KeyPress-Left>',lambda event :self.bowl.move("left"))
		self.interface.getMenu().TkMenu.bind('<KeyPress-Right>',lambda event :self.bowl.move("right"))
  
		

game=Game()
