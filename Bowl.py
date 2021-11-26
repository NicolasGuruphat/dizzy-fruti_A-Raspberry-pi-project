
from tkinter import *
from PIL import ImageTk,Image
class Bowl:
    def __init__(self, menu):
        self.menu=menu
        self.TkMenu=menu.TkMenu
        print(self.menu.getName())
        print("bowl initialized")
        path = "sprite/sprite_bowl.png"
        canvas = Canvas(self.TkMenu, bg="white", width=133, height=133)
        imageBowl = ImageTk.PhotoImage(master=self.TkMenu,file="sprite/sprite_bowl.png")
        canvas.image=imageBowl
        canvas.grid(row=0,column=0)
        canvas.create_image(100,100, anchor=NW,image = canvas.image)
        
   
   
           #     self.display()
    
#    def display(self):

       

