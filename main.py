from tkinter import *

class Game:
	def __init__(self):
		interface=UI()
		#instaciate other stuff
		interface.root.mainloop()
		
	@staticmethod
	def play():
		print("jeu lancé")


class UI:

	def __init__(self):
		
		self.root = Tk()
		self.listComposant=[]
		self.buttonPlay = Button(text="Play",background="lightgreen", command=Game.play())
		self.fill()

	def fill(self): 
		self.buttonPlay.grid(row=0,column=0)
		self.addToList(self.buttonPlay)


	def addToList(self,composant):
		self.listComposant.append(composant)

	def flush(self):
		for composant in self.listeComposant:
			composant.destroy()


game=Game()
