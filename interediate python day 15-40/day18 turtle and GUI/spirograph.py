from turtle import Turtle, Screen
from random import random


def random_color():
    """random color generatig function.

    Returns:
        tuple: returns tuple (r, g, b), where r, g, b are the random float number range from 0, 1.
    """
    r = random()
    g = random()
    b = random()
    return (r, g, b)


tim = Turtle()
tim.speed("fastest")
tim.pensize(1)
def spirogram(size_of_gap):    
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

spirogram(5)
screen = Screen()
screen.exitonclick()
