from tkinter import *
from UI import UI
from Bowl import Bowl
class Game:

	def __init__(self):
		self.interface=UI(self)
		self.interface.displayMainMenu()
		self.interface.root.mainloop()
		
	
	def play(self):
		print("jeu lancé")
		self.interface.hideMainMenu()
		self.interface.displayGameMenu()
		self.bowl=Bowl(self.interface.getMenu())


game=Game()
