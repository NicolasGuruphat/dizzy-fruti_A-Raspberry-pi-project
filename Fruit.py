from tkinter import *
from PIL import ImageTk,Image
from random import *

class Fruit : 
	
	def __init__(self,menu): 
		randomInt=randint(1,100)
		self.menu=menu
		self.TkMenu=menu.TkMenu
		self.canvas=self.menu.canvas
		path="sprite/sprite_strawberry.png"
		if 1 <= randomInt <= 10 : 
			path = "sprite/sprite_strawberry.png"
			self.taille = 24
	        

		if 11 <= randomInt <= 30 :
			path = "sprite/sprite_lemon.png"
			self.taille = 32
	        

		if 31 <= randomInt <= 70 :
			path = "sprite/sprite_apple.png"
			self.taille = 48
	       

		if 71 <= randomInt <= 90 :
			path = "sprite/sprite_orange.png"
			self.taille = 64

		if 91 <= randomInt <= 100 :
			path = "sprite/sprite_watermelon.png"
			self.taille = 96




		self.imageFruit = ImageTk.PhotoImage(master=self.TkMenu,file="sprite/sprite_watermelon.png")
		self.canvas.image=self.imageFruit
		self.fuitItem=self.canvas.create_image(0,0, anchor=NW,image = self.canvas.image)

		randomInt=randint(0,menu.taille[0]-(self.taille))
		
		self.canvas.moveto(self.fuitItem,randomInt,0) #set random x position on top of the screen 

		def moveDown(self) : 

			self.menu.canvas.move(self.bowlItem,0,20-(self.taille)/8)

