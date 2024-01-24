from turtle import Turtle, Screen
little_turtle = Turtle()
# little_turtle.shape("turtle")
# little_turtle.color("violet")
# for _ in range(4):
#     for steps in range(0, 100, 5):
#         for c in ('blue', 'red', 'green'):
#             little_turtle.color(c)
#             little_turtle.forward(steps)
#             little_turtle.right(120)
#     little_turtle.left(80)

# screen = Screen()
# screen.exitonclick()


little_turtle.shape("arrow")
little_turtle.color("blue")

for _ in range(15):
    little_turtle.fd(10)
    little_turtle.penup()
    little_turtle.fd(10)
    little_turtle.pendown()

screen = Screen()
screen.exitonclick()