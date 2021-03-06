from tkinter import *
from Menu import MainMenu,GameMenu,WinMenu,Root, LooseMenu

class UI:

	def __init__(self,game):
		self.game=game
		self.root=Root(game)
		self.menu=self.root
		self.menu.hide()
		self.mainMenu=MainMenu(game)
		self.gameMenu=GameMenu(game)
		self.winMenu=WinMenu(game)
		self.looseMenu=LooseMenu(game)
	def displayMainMenu(self):
		self.menu.hide()
		self.mainMenu.display()
		print("main menu displayed")
		self.menu=self.mainMenu

	def displayGameMenu(self):
		self.menu.hide()
		self.gameMenu.display()
		print("game menu displayed")
		self.menu=self.gameMenu

	def displayWinMenu(self):
		self.menu.hide()
		self.winMenu.display()
		print("win menu displayed")
		self.menu=self.winMenu

	def displayLooseMenu(self):
			self.menu.hide()
			self.looseMenu.display()
			print("win menu displayed")
			self.menu=self.looseMenu

	def getMenu(self):
		return self.menu
