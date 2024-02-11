from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.listen()
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    # detect collision with wall
    if ball.ycor() > 289 or ball.ycor() < -289:
        ball.bounce_y()
    # detect collision with paddles
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 330
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -330
    ):
        ball.bounce_x()


    # detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_ball()
        score.r_update()
    # detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_ball()
        score.l_update()


screen.exitonclick()
