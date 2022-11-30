import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score_board import Scoreboard

screen = Screen()
screen.setup(width= 600, height= 600)
screen.tracer(0)

tim = Player()

cars = CarManager()
cars.create_cars()

score = Scoreboard()

screen.listen()
screen.onkey(tim.up, "Up")

game_is_on = True

while game_is_on:
	time.sleep(0.1)	
	screen.update()
	cars.move()

	#Detect coliision with cars
	for car in cars.all_cars:
		if car.distance(tim) < 20:
			game_is_on = False
			score.game_over()

	#Detect crossing
	if tim.ycor() == 300:
		tim.restart()
		cars.car_speed()
		score.increase_score()

screen.exitonclick()
