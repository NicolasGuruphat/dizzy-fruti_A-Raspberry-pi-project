from tkinter import *
from Menu import MainMenu,GameMenu

class UI:

	def __init__(self,game):
		self.game=game
		self.root=Tk()
		self.root.title("root")
		self.menu=self.root
		self.root.withdraw()
		self.mainMenu=MainMenu(game)
		self.gameMenu=GameMenu(game)

	def displayMainMenu(self):
		self.mainMenu.display()
		print("main menu displayed")
		self.menu=self.getMenu()

	def displayGameMenu(self):
		self.gameMenu.display()
		print("game menu displayed")
		self.menu=self.gameMenu.getMenu()

	def hideGameMenu(self):
		self.gameMenu.hide()

	def hideMainMenu(self):
		self.mainMenu.hide()
	def getMenu(self):
		
		print("get menu")
		return self.menu
