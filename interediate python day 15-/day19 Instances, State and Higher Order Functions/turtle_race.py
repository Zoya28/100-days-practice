from turtle import Turtle, Screen
from random import randint

color = ["blue", "green", "yellow", "red", "orange", "pink"]
game_is_on = False
screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(
title="betting competition", prompt=f'''chose a color of your turtle from this list.
{color}'''
)
all_turtles = []
y = 90

if user_bet:
    game_is_on = True

for turtles in range(6):
    players = Turtle(shape="turtle")
    players.color(color[turtles])
    players.penup()
    players.setpos(-280, y)
    y -= 30
    all_turtles.append(players)

while game_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 280:
            game_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! {winning_color} turtle is a winner!")
            else:
                print(f"you've loose! {winning_color} turtle is a winner!")
        random_pace = randint(0, 10)
        turtle.forward(random_pace)

screen.exitonclick()
