from turtle import Turtle, Screen

tomy = Turtle()
tomy.color("red")
tomy.pensize(3)
def move_forward():
    tomy.forward(10)
def move_backward():
    tomy.backward(10)
def move_forward():
    tomy.forward(10)
def move_forward():
    tomy.forward(10)
def move_anti_clockwise():
    tomy.setheading(tomy.heading() + 10)
def move_clockwise():
    tomy.setheading(tomy.heading() - 10)
def clear_screen():
    screen.reset()
    
screen = Screen()
screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=move_anti_clockwise)
screen.onkeypress(key="d", fun=move_clockwise)
screen.onkeypress(key="c", fun=clear_screen)
screen.exitonclick()
