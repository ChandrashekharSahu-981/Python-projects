from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Score()

screen.listen()

screen.onkeypress(r_paddle.start_up, "Up")
screen.onkeyrelease(r_paddle.stop_up, "Up")

screen.onkeypress(r_paddle.start_down, "Down")
screen.onkeyrelease(r_paddle.stop_down, "Down")

screen.onkeypress(l_paddle.start_up, "w")
screen.onkeyrelease(l_paddle.stop_up, "w")

screen.onkeypress(l_paddle.start_down, "s")
screen.onkeyrelease(l_paddle.stop_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    r_paddle.move()
    l_paddle.move()
    ball.ball_move()

    #Detecting collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    #Detecting collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detecting paddle miss
    if ball.xcor() > 380:
        ball.restart()
        score.inc_l_score()

    if ball.xcor() < -380:
        ball.restart()
        score.inc_r_score()

screen.exitonclick()