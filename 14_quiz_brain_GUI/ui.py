from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

	def __init__(self, quiz_brain:QuizBrain) -> None:

		self.quiz = quiz_brain
		score = 0
		self.window = Tk()
		self.window.title("Quizzler")
		self.window.config(bg=THEME_COLOR, padx=20, pady=20)

		self.lbl = Label(text=f"Score:{score}", fg="white")
		self.lbl.config(font=("Arial", 12, "bold"), background=THEME_COLOR)
		self.lbl.grid(row=0, column=1)

		self.canvas = Canvas(width=300, height=250, bg="white")
		self.canvas_text = self.canvas.create_text(
			150, 
			125,
			width=280,
			fill=THEME_COLOR, 
			font=("Arial", 20, "italic"))
		self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

		img_btn_check = PhotoImage(file="14_quiz_brain_GUI/img/true.png")
		self.check_btn = Button(
			image=img_btn_check, 
			highlightthickness=0,
			command=self.true_pressed)
		self.check_btn.grid(row=2, column=0)

		img_btn_cross = PhotoImage(file="14_quiz_brain_GUI/img/false.png")
		self.wrong_btn = Button(
			image=img_btn_cross, 
			highlightthickness=0,
			command= self.false_pressed)
		self.wrong_btn.grid(row=2, column=1)

		self.get_next_question()
		self.window.mainloop()

	def get_next_question(self):
		self.canvas.config(bg="white")

		if self.quiz.still_has_question():
			self.lbl.config(text=f"Score:{self.quiz.score}")
			q_text = self.quiz.next_cuestion()
			self.canvas.itemconfig(self.canvas_text, text=q_text)
		else:
			self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the questions")
			self.check_btn.config(state="disabled")
			self.wrong_btn.config(state="disabled")


	def true_pressed(self):
		self.give_feedback(self.quiz.check_answer("True"))
	
	def false_pressed(self):
		self.give_feedback(self.quiz.check_answer("False"))

	def give_feedback(self,is_right):
		if is_right:
			self.canvas.config(bg="green")
		else:	
			self.canvas.config(bg="red")

		self.window.after(1000, self.get_next_question)
		