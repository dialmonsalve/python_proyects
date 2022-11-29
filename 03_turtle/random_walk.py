from turtle import Turtle, Screen
import turtle as t
from random import randint, choice

def draw_shape(timmy:Turtle):
	move = randint(1,31)
	directions = [0, 90, 180, 270]
	timmy.forward(move)
	timmy.setheading(choice(directions))

def random_color():
	r = randint(1,255)
	g = randint(1,255)
	b = randint(1,255)
	return  (r,g,b)

t.colormode(255)

timmy = Turtle()
timmy.shape('turtle')
timmy.pensize(10)
timmy.speed(0)

num_sides = 0

while num_sides <= 100:

	timmy.color(random_color())
	draw_shape(timmy)

	num_sides += 1

screen = Screen()
screen.exitonclick()