from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

snake = Snake()
food = Food()
score = Scoreboard()
screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Down", fun=snake.down)
screen.onkeypress(key="Left", fun=snake.left)
screen.onkeypress(key="Right", fun=snake.right)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()

    # detect collision of food
    if snake.head.distance(food) < 15:
        food.random_position()
        snake.extend()
        score.increase_score()

    # detect collision of walls
    if snake.head.xcor() > 240 or snake.head.xcor() < -250 or snake.head.ycor() > 240 or snake.head.ycor() < -250 :
        game_is_on = False
        score.game_over()

    # collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
screen.exitonclick()
