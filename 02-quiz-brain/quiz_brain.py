class QuizBrain:
	""" Its constructor Wait for a list and that list must contain a dictionary """
	def __init__(self, question_list: list) -> None:
		self.question_number:int = 0
		self.question_list:list = question_list
		self.score:int = 0

	def still_has_question(self) -> bool:
		return self.question_number < len(self.question_list)
	
	def next_cuestion(self) -> None:
		current_question = self.question_list[self.question_number]
		self.question_number+=1
		user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
		self.check_answer(user_answer, current_question.answer)

	def check_answer(self, user_answer:str, current_answer:str):
		if user_answer.lower() == current_answer.lower():
			self.score+=1
			print(f"You got it right")
		else:
			print(f"Thats wrong")
		print(f"The correct answer was {current_answer}")
		print(f"your current score is {self.score}/{self.question_number}\n")