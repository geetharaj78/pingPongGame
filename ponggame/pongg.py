from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
import random
from scoreboard import Scoreboard
#creating the screen.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # for us to turn of the animation.

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()

#for the screen to listen to our commands when pressed any keys
screen.listen()
screen.onkey(right_paddle._up, "Up")
screen.onkey(right_paddle._down, "Down")
screen.onkey(left_paddle._up, "w")
screen.onkey(left_paddle._down, "x")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move() #we got the ball to move on every refresh of the screen.

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detects right padding misses.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        #detects left padding misses.
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()

