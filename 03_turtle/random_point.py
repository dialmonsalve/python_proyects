import turtle as t
from turtle import Turtle, Screen
from random import choice

def points(turtle:Turtle, x):

	turtle.hideturtle()
	turtle.speed(0)
	turtle.penup()
	
	eje_y = x * 20
	for j in range(1 , x+1):
		turtle.sety(-eje_y + 20 * j)

		eje_x = x * 20
	
		turtle.goto(-eje_x ,-eje_y)
		for i in range(1, x+1):
			turtle.setx(-eje_x + 20 * i)
			turtle.begin_fill()
			turtle.fillcolor(choice(color_list))
			turtle.circle(10)
			turtle.end_fill()
			turtle.goto(-eje_x,-eje_y)

			eje_x-=20
		eje_y-=40

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

t.colormode(255)

tim = Turtle("circle")

points(tim, 15)

screen = Screen()
screen.exitonclick()


