from turtle import Turtle, Screen
from random import choice, random

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
tim.pensize(10)
tim.speed(8)
tim_pos = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random_color())
    tim.circle
    tim.setheading(choice(tim_pos))
    tim.fd(30)


screen = Screen()
screen.exitonclick()
