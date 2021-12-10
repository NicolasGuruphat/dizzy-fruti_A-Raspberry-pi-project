#from sense_hat import SenseHat

class RaspberrySenseHat:
    
    def __init__(self):
        self.lastLed=0
        #self.sense=SenseHat()
        X = [255, 255, 255]
        O = [0,0,0]
        self.matrix = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ]
        #self.sense.set_pixels(self.question_mark)

    def add(self,color, point):
        self.matrix[self.lastLed]=color
        self.lastLed+=1
        print(self.matrix)
        #self.sense.set_pixels(self.question_mark)

        