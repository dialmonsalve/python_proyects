from turtle import Turtle, Screen

def draw_shape(timmy:Turtle, num_sides):
	angle = 360 / num_sides
	timmy.forward(100)
	timmy.right(angle)

timmy = Turtle()
timmy.shape('turtle')

num_sides = 3

while num_sides <= 10:
	for i in range(1, num_sides + 1):
		timmy.color("#285078", "#a0c8f0")
		draw_shape(timmy,num_sides)
	num_sides += 1



screen = Screen()
screen.exitonclick()

