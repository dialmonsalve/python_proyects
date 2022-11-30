from turtle import Turtle

FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
	def __init__(self) -> None:
		super().__init__()

		self.score = 1

		self.hideturtle()
		self.color("black")
		self.penup()
		self.goto(0,270)
		self.update_scorebord()

	def update_scorebord(self):
		self.write(f" Level {self.score}",align="center", font= FONT)

	def game_over(self):
		self.goto(0, 0)
		self.write(f"GAME OVER",align="center", font= FONT)

	def increase_score(self):
		
		self.score +=1
		self.clear()
		self.update_scorebord()