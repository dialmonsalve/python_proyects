from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)

screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)


right_paddle = Paddle(350)
left_paddle = Paddle(-350)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
	time.sleep(ball.speed_ball)
	screen.update()
	ball.move()

	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()

	if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
		ball.bounce_x()

	#Detect Right paddle misses
	if ball.xcor() > 400:
		scoreboard.left_increase_score()
		ball.reset()

	
	#Detect Left paddle misses
	if ball.xcor() < -400:
		scoreboard.right_increase_score()
		ball.reset()


screen.exitonclick()