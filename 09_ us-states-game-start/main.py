import pandas
import turtle

def search_state(answer_state, state_list):
	for state in state_list:
		if answer_state == state:
			guessed_state.append(answer_state)
			t = turtle.Turtle()
			t.penup()
			t.hideturtle()
			t.goto(state_list[1], state_list[2])
			t.write(state, move=True, align="center")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "09_ us-states-game-start/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("09_ us-states-game-start/50_states.csv")

guessed_state = []
while len(guessed_state) < 50 :
	answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", 
		prompt="What's another state's name?").title()

	row = data[data.state == answer_state].to_dict()

	state_list =[]

	for k,v in row.items():
		for x, y in v.items():
			state_list.append(y)

	""" def get_mouse_click_coor(x, y):
		print(x, y)

	turtle.onscreenclick(get_mouse_click_coor)"""
	search_state(answer_state, state_list) 

	if answer_state == "Exit":
		missing_states = [state for state in state_list if state not in guessed_state]
		new_data = pandas.DataFrame(missing_states)
		new_data.to_csv("09_ us-states-game-start/states_to_learn.csv")
		break

	



