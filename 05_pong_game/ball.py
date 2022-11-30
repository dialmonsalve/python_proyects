from turtle import Turtle

class Ball(Turtle):

	def __init__(self)-> None:
		super().__init__()

		self.penup()
		self.shape("circle")
		self.color("red")
		self.x_move = 10
		self.y_move = 10
		self.speed_ball = 0.1

	def move(self):
		new_x = self.xcor() + self.x_move
		new_y = self.ycor() + self.y_move
		
		self.goto(new_x, new_y)
	
	def bounce_y(self):
		self.y_move *= -1
		
	def bounce_x(self):
		self.x_move *= -1
		self.speed_ball *=0.9

	def reset(self):

		self.goto(0, 0)
		self.bounce_x()
		self.speed_ball = 0.1


		
		

