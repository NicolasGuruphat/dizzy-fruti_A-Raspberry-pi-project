from tkinter import *
from UI import UI

class Game:

	def __init__(self):
		self.interface=UI(self)
		#instaciate other stuff
		self.interface.displayMainMenu()
		self.interface.root.mainloop()
	
	def play(self):
		print("jeu lancé")
		self.interface.displayGameMenu()
		self.interface.hideMainMenu()

game=Game()
