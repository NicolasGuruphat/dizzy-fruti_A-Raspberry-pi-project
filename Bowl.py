
from tkinter import *
from PIL import ImageTk,Image

class Bowl:
    def __init__(self, menu):
        self.menu=menu
        self.TkMenu=menu.TkMenu
        path = "sprite/sprite_bowl.png"
        self.canvas = Canvas(self.TkMenu, bg="white", width=menu.taille[0], height=menu.taille[1])
        self.imageBowl = ImageTk.PhotoImage(master=self.TkMenu,file=path)
        self.canvas.image=self.imageBowl
        self.canvas.grid(row=0,column=0)
        self.bowlItem=self.canvas.create_image(0,0, anchor=NW,image = self.canvas.image)
        
        self.canvas.moveto(self.bowlItem,(menu.taille[0]-132)/2,menu.taille[1]-90) #set default position 

    def move(self,direction):
        print(self.canvas.coords(self.bowlItem))
        if direction == "left" and self.canvas.coords(self.bowlItem)[0]>25:
            self.canvas.move(self.bowlItem,-25,0)
        if direction == "right" and self.canvas.coords(self.bowlItem)[0]<self.menu.taille[1]+132/2:
            self.canvas.move(self.bowlItem,25,0)


