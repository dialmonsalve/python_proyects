from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
	def __init__(self ) -> None:
		super().__init__()

		self.shape("turtle")
		self.left(90)
		self.penup()
		self.color("black", "red")
		self.restart()

	def up(self):
		new_y =self.ycor() + MOVE_DISTANCE
		self.goto(0, new_y)

	def restart(self):		
		self.goto(STARTING_POSITION)
