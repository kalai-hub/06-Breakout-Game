# paddle.py
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.xcoordinates = coordinates[0]
        self.ycoordinates = coordinates[1]
        self.goto(self.xcoordinates, self.ycoordinates)

    def left(self):
        self.backward(20)

    def right(self):
        self.forward(20)