from tkinter import *
from UI import UI
from Bowl import Bowl

class Game:

	def __init__(self):
		self.interface=UI(self)
		self.interface.displayMainMenu()
		self.interface.root.TkMenu.mainloop()
		
	
	def play(self):
		print("Play !")
		self.interface.displayGameMenu()
		self.bowl=Bowl(self.interface.getMenu())
		self.interface.getMenu().TkMenu.bind('<KeyPress-Left>',lambda event :self.bowl.move("left"))
		self.interface.getMenu().TkMenu.bind('<KeyPress-Right>',lambda event :self.bowl.move("right"))

	def win(self):
		print("well play ! you won")
		self.interface.displayWinMenu()
		
game=Game()
