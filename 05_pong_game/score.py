from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")

class Scoreboard(Turtle):
	
	def __init__(self) -> None:
		super().__init__()

		self.left_score = 0
		self.right_score = 0

		self.hideturtle()
		self.color("blue", "red")
		self.penup()		
		self.update_scorebord()
	
	def update_scorebord(self):
		self.clear()
		self.goto(-100,240)
		self.write(f"{self.left_score}",align=ALIGNMENT, font= FONT)
		self.goto(100,240)
		self.write(f"{self.right_score}",align=ALIGNMENT, font= FONT)

	def left_increase_score(self):
		
		self.left_score+=1
		self.update_scorebord()

	def right_increase_score(self):
		
		self.right_score+=1
		self.update_scorebord()