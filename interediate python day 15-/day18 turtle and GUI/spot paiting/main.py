""" Importing colorgram module to extract colours from the image and save it in the list."""

# import colorgram
# colors = colorgram.extract("C:/Users/Soft/OneDrive/Documents/GitHub/100-days-practice/interediate python day 15-/day18 turtle and GUI/spot paiting/image.jpg", 30)
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color = (r, g, b)
#     color_list.append(color)
# print(color_list)

from turtle import Turtle, Screen, colormode
from random import choice
colors = [
    (236, 121, 43),(123, 70, 49),(181, 219, 242),(1, 1, 1),(6, 135, 187),(246, 90, 178),(147, 175, 73),(188, 55, 57),(239, 212, 2),(226, 210, 68),(241, 87, 172),(114, 178, 199),(237, 165, 204),(1, 1, 3),(1, 2, 1),(71, 145, 170),(5, 3, 4),(178, 100, 91),(150, 207, 225),(227, 175, 170),(84, 62, 41),(76, 78, 76),(164, 166, 165),
]
colormode(255)
tim = Turtle()
tim.hideturtle()
tim.penup()
y = -200
tim.setposition(-300, y)
tim.speed("fastest")
for _ in range(10):
    for _ in range(10):
        tim.dot(20, choice(colors))
        tim.penup()
        tim.fd(50)
        tim.pendown()
    y += 50
    tim.penup()
    tim.setpos(-300, y)
    tim.pendown()

screen = Screen()
screen.exitonclick()
