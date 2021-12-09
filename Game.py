from tkinter import *
from UI import UI
from Bowl import Bowl
from Fruit import Fruit
from Score import Score
import threading
from time import *
from random import randint

class Game:

	def __init__(self):
		
		self.interface=UI(self)
		self.interface.displayMainMenu()
		self.listFruit=[]
		self.interface.root.TkMenu.mainloop()

	def fruitFactory(self) : 
		self.listFruit.append(Fruit(self.interface.getMenu()))
		
		self.interface.getMenu().TkMenu.after(1000,self.fruitFactory)
			
	def fruitFalling(self) : 
		for i in  range (len(self.listFruit)) :
			Fruit.moveDown(self.listFruit[i],self.interface)
		self.interface.getMenu().TkMenu.after(60,self.fruitFalling)

	def play(self):
		print("Play !")
		self.interface.displayGameMenu()
		self.bowl=Bowl(self.interface.getMenu())
		self.interface.getMenu().TkMenu.bind('<KeyPress-Left>',lambda event :self.bowl.move("left"))
		self.interface.getMenu().TkMenu.bind('<KeyPress-Right>',lambda event :self.bowl.move("right"))
		self.score=Score()
		self.fruitFactory()
		self.fruitFalling()
		print("here")
		
			


#		self.t=threading.Thread(target=self.fruitFactory)
#		self.t.start()

	def win(self):
		print("well play ! you won")
		self.interface.displayWinMenu()

class ThreadedTask(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        time.sleep(5)  # Simulate long running process
        self.queue.put("Task finished")


game=Game()




