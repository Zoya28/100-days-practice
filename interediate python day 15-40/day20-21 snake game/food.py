from turtle import Turtle
from random import randint
class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.penup()
        
    def random_position(self):
        random_x = randint(-230, 230)
        random_y = randint(-230, 230)
        self.goto(random_x, random_y)