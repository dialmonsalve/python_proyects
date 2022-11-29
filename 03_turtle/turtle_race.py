from turtle import Turtle, Screen
from random import randint

num_random = randint(1, 5)
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Wich turtle will win the race?, Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtle=[]

pos=60
for index in range(0, 6):	

	new_turtle = Turtle(shape="turtle")
	new_turtle.penup()
	new_turtle.color(colors[index])
	new_turtle.goto(x=-230, y=pos)

	all_turtle.append(new_turtle)
	
	pos-=30

if user_bet:
	is_race_on=True

while is_race_on:

	for turtle in all_turtle:
		if turtle.xcor() > 230:
			winnig_race = turtle.pencolor()
			if winnig_race == user_bet :
				print("Congrats!, you are the win")
			else:
				print("Sorry!, you lose")
			is_race_on=False
		num = randint(0, 10)
		race = turtle.forward(num)

		
		



screen.exitonclick()
