from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1

class CarManager():
	def __init__(self) -> None:
		super().__init__()

		self.all_cars = []
		self.speed = STARTING_MOVE_DISTANCE

	def create_cars(self):

		for car in range(1 , 35):

			car = Turtle("square")
			car.shapesize(stretch_len=2, stretch_wid=1)
			car.penup()
			car.color(choice(COLORS))

			rand_x = randint(-280, 280)
			rand_y = randint(-250, 240)
			
			car.goto(rand_x, rand_y)
			
			self.all_cars.append(car)

	def move(self):
		for car in self.all_cars:
			car.backward(self.speed)

			rand_y = randint(-250, 280)

			if car.xcor() < -320 :
				car.goto(300, rand_y)
	
	def car_speed(self):
		self.speed  += MOVE_INCREMENT


