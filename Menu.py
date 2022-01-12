from tkinter import Tk, Button, Canvas, Label

class Menu:
	def __init__(self,game,title):
		self.game=game
		self.listComponant=[]
		self.TkMenu=Tk()
		self.TkMenu.withdraw()
		self.TkMenu.title(title)
		self.taille=[720,480]
		self.TkMenu.minsize(self.taille[0],self.taille[1])

	def popComponent(self,componant):
		self.listComponant.pop(componant)
		componant.destroy()

	def addComponent(self,componant):
		self.listComponant.append(componant)
		
	def display(self):
		self.TkMenu.deiconify() 
			
	def hide(self):
		self.TkMenu.withdraw()
		
	def getMenu(self):
		return self
	
	def getName(self):
		return self.TkMenu.title()

	def hide(self):
		self.TkMenu.withdraw()

class MainMenu(Menu):

	def __init__(self,game):
		super().__init__(game,"main menu")
		self.buttonPlay = Button(self.TkMenu,text="Play",background="lightgreen", height=40, width=120, command=lambda :game.play())
		self.buttonPlay.grid(row=0,column=0)
		
			
class GameMenu(Menu):

	def __init__(self,game):
		super().__init__(game,"game menu")
		self.canvas = Canvas(self.TkMenu, bg="white", width=self.taille[0]-100, height=self.taille[1])
		self.canvas.grid(row=0,column=1)
		self.canvasVie= Canvas(self.TkMenu, bg="yellow", width=100, height=self.taille[1])
		self.canvasVie.grid(row=0,column=0)
		self.canvasVie1=Canvas(self.canvasVie, bg="green",width=100, height=self.taille[1]/3)
		self.canvasVie1.grid(row=0,column=0)
		self.canvasVie2=Canvas(self.canvasVie, bg="yellow",width=100, height=self.taille[1]/3)
		self.canvasVie2.grid(row=1,column=0)
		self.canvasVie3=Canvas(self.canvasVie, bg="red",width=100, height=self.taille[1]/3)
		self.canvasVie3.grid(row=3,column=0)
		#self.buttonWin= Button(self.canvas, text="win",command=lambda: game.win()) 
		#self.buttonWin.grid(row=1,column=1)

class WinMenu(Menu):

	def __init__(self,game):
		super().__init__(game,"win menu")
		self.canvas = Canvas(self.TkMenu, bg="white", width=self.taille[0], height=self.taille[1])
		self.canvas.grid(row=0,column=0)
		self.label = Label(self.canvas, text="WIN !")
		self.label.config(font=("Courier", 250))
		self.label.grid(row=0,column=0)

class LooseMenu(Menu):

	def __init__(self,game):
		super().__init__(game,"win menu")
		self.canvas = Canvas(self.TkMenu, bg="white", width=self.taille[0], height=self.taille[1])
		self.canvas.grid(row=0,column=0)
		self.label = Label(self.canvas, text="Loose !")
		self.label.config(font=("Courier", 250))
		self.label.grid(row=0,column=0)

class Root(Menu):
	def __init__(self,game):
		super().__init__(game,"root")