from tkinter import *
class game:
	def __init__(self):
		interface=UI()
		#instaciate other stuff
		interface.root.mainloop()



class UI:

	def __init__(self):
		self.root = Tk();
		self.button
		self.fill()
	def fill(self):
		self.button = Button(text="Play",background="lightgreen")

		self.button.grid(row=0,column=0)
print("test forge")
Game=game()
