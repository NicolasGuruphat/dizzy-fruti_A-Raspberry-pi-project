from tkinter import *

class menu:
	def __init__(self,game):
		self.game=game
		self.listComposant=[]
		self.menu=Tk()
		self.menu.withdraw()

	def flush(self):
		for composant in self.listComposant:
			composant.destroy()

	def display(self):
			self.menu.deiconify() 
			
	def hide(self):
			self.menu.withdraw()


class UI:

	class MainMenu(menu):

		def __init__(self,game):
			
			super().__init__(game)
			self.buttonPlay = Button(self.menu,text="Play",background="lightgreen", command=lambda :game.play())
			self.buttonPlay.grid(row=0,column=0)
		
			
	class GameMenu(menu):

		def __init__(self,game):
			super().__init__(game)


	def __init__(self,game):
		self.game=game
		self.root=Tk()
		self.root.withdraw()
		self.mainMenu=UI.MainMenu(game)
		self.gameMenu=UI.GameMenu(game)

	def displayMainMenu(self):
		self.mainMenu.display()

	def displayGameMenu(self):
		self.gameMenu.display()

	def hideGameMenu(self):
		self.gameMenu.hide()

	def hideMainMenu(self):
		self.mainMenu.hide()

