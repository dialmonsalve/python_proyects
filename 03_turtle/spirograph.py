from turtle import Turtle,done
import turtle as t
from random import randint, choice

def spirograph(turtle:Turtle, angle):

	num_turns = 360/angle
	tot = 360/angle

	while num_turns <= 360 + tot:

		turtle.color(random_color())
		turtle.circle(100)
		turtle.right(angle)

		num_turns+=angle

def random_color():
	r = randint(1,255)
	g = randint(1,255)
	b = randint(1,255)
	return  (r,g,b)
t.colormode(255)

timmy = Turtle()
timmy.speed(0)


spirograph(timmy, 10)

timmy.begin_fill()

timmy.end_fill()
done()