from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
	tim.forward(10)

def move_back():
	tim.backward(10)

def turn_left():
	tim.left(45)

def turn_right():
	tim.right(45)

def clear():
	tim.clear()
	tim.penup()
	tim.home()
	tim.pendown()


screen.listen()
screen.onkey(move_forwards, "d")
screen.onkey(move_back,"a")
screen.onkey(turn_left, "w")
screen.onkey(turn_right, "s")
screen.onkey(clear, "c")
screen.exitonclick()