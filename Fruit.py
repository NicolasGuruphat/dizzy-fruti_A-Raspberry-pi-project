from tkinter import *
from PIL import ImageTk,Image
from random import *

class Fruit : 
	
	def __init__(self,menu): 
		randomInt=randint(1,100)
		self.menu=menu
		self.TkMenu=menu.TkMenu
		self.canvas=self.menu.canvas
		self.point=1
		self.color =[0, 0, 0]
		path="sprite/sprite_strawberry.png"
		if 1 <= randomInt <= 10 : 
			path = "sprite/sprite_strawberry.png"
			self.taille = 24
			self.color =[255, 100, 100]

		if 11 <= randomInt <= 30 :
			path = "sprite/sprite_lemon.png"
			self.taille = 32
			self.color =[255, 247, 0]   
		if 31 <= randomInt <= 70 :
			path = "sprite/sprite_apple.png"
			self.taille = 48
			self.color =[255, 0, 0]

		if 71 <= randomInt <= 90 :
			path = "sprite/sprite_orange.png"
			self.taille = 64
			self.color =[255, 149, 0]
		if 91 <= randomInt <= 100 :
			path = "sprite/sprite_watermelon.png"
			self.taille = 96
			self.color =[89, 255, 0]


		self.speed=12-((self.taille)/10)
		self.imageFruit = ImageTk.PhotoImage(master=self.TkMenu,file=path)
		self.canvas.image=self.imageFruit
		self.fruitItem=self.canvas.create_image(0,0, anchor=NW,image = self.canvas.image)

		randomInt=randint(0,menu.taille[0]-(self.taille))
		
		self.canvas.move(self.fruitItem,randomInt,0) #set random x position on top of the screen 

	def moveDown(self, interface) : 
		self.canvas.move(self.fruitItem,0,self.speed)

	def verifyCollisionBowl(self,bowl):
		
		fruitPosition = self.canvas.coords(self.fruitItem)
		bowlPosition = bowl.bowlPosition
		return (( (fruitPosition[0] + self.taille) > bowlPosition[0]) and  (fruitPosition[0] < bowlPosition[0] + bowl.bowlSize[0]) and ((fruitPosition[1]+ self.taille) > bowlPosition[1]))

	def verifyCollisionGround(self,menuSize):
		fruitPosition = self.canvas.coords(self.fruitItem)
		return (fruitPosition[1]>menuSize[1]-self.taille )


		
