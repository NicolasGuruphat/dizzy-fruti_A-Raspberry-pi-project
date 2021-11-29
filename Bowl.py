from tkinter import *
from PIL import ImageTk,Image

class Bowl:
    def __init__(self, menu):
        self.menu=menu
        self.TkMenu=menu.TkMenu
        self.canvas=self.menu.canvas

        path = "sprite/sprite_bowl.png"
        self.imageBowl = ImageTk.PhotoImage(master=self.TkMenu,file=path)
        self.canvas.image=self.imageBowl
        self.canvas.grid(row=0,column=0)
        self.bowlItem=self.canvas.create_image(0,0, anchor=NW,image = self.canvas.image)

        self.canvas.moveto(self.bowlItem,(menu.taille[0]-132)/2,menu.taille[1]-90) #set default position 

    def move(self,direction):
        if direction == "left" and self.canvas.coords(self.bowlItem)[0]>25:#check of the position and direction
            self.menu.canvas.move(self.bowlItem,-25,0)
        if direction == "right" and self.canvas.coords(self.bowlItem)[0]<self.menu.taille[1]+132/2:#check of the position and direction
            self.menu.canvas.move(self.bowlItem,25,0)


