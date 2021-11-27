from tkinter import Tk, Button, Canvas

class Menu:
    def __init__(self,game,title,nom):
        self.game=game
        self.listComponant=[]
        self.TkMenu=Tk()
        self.TkMenu.withdraw()
        self.TkMenu.title(title)
        self.nom=nom
        self.taille=[720,480]
        self.TkMenu.minsize(self.taille[0],self.taille[1])
    def flush(self):
        for composant in self.listComponant:
            composant.destroy()

    def display(self):
	    self.TkMenu.deiconify() 
			
    def hide(self):
	    self.TkMenu.withdraw()
		
    def getMenu(self):
	    return self
    
    def getName(self):
        return self.TkMenu.title()

class MainMenu(Menu):

	def __init__(self,game):
		super().__init__(game,"main menu","mainMenu")
		self.buttonPlay = Button(self.TkMenu,text="Play",background="lightgreen", height=40, width=120, command=lambda :game.play())
		self.buttonPlay.grid(row=0,column=0)
		
			
class GameMenu(Menu):

    def __init__(self,game):
        super().__init__(game,"game menu","gameMenu")
        self.nom="game menu"
        self.canvas = Canvas(self.TkMenu, bg="white", width=self.taille[0], height=self.taille[1])