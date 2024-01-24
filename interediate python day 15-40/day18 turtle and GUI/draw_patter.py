from turtle import Turtle, Screen
from random import choice

colors = [
    "light steel blue",
    "dodger blue",
    "green yellow",
    "maroon",
    "peach puff",
    "brown",
    "tomato",
    "crimson",
    "dark magenta",
    "thistle",
    "indigo",
]

tim = Turtle()
tim.shape("classic")

sides = 3
while sides <= 10:
    for _ in range(sides):
        tim.color(choice(colors))
        angle = 360 / sides
        tim.right(angle)
        tim.fd(100)
    sides += 1

screen = Screen()
screen.exitonclick()
