from tkinter import *
from PIL import ImageTk,Image

class Bowl:

    def __init__(self, menu):
        self.menu=menu
        self.TkMenu=menu.TkMenu
        self.canvas=self.menu.canvas
        self.bowlSize=[132,90]
        self.bowlPosition=[]
        path = "sprite/sprite_bowl.png"
        self.imageBowl = ImageTk.PhotoImage(master=self.TkMenu,file=path)
        self.canvas.image=self.imageBowl
        self.bowlItem=self.canvas.create_image(0,0, anchor=NW,image = self.canvas.image)
        self.canvas.moveto(self.bowlItem,(menu.taille[0]-self.bowlSize[0])/2,menu.taille[1]-self.bowlSize[1]) #set default position 
        self.bowlPosition=self.menu.canvas.coords(self.bowlItem)
        #useless ? self.menu.addComponent(self.bowlItem)

    def move(self,direction):
        if direction == "left" and self.canvas.coords(self.bowlItem)[0]>25:#check of the position and direction
            self.menu.canvas.move(self.bowlItem,-25,0)
        if direction == "right" and self.canvas.coords(self.bowlItem)[0]<self.menu.taille[1]+self.bowlSize[0]/2:#check of the position and direction
            self.menu.canvas.move(self.bowlItem,25,0)
        self.bowlPosition=self.menu.canvas.coords(self.bowlItem)
    

