import html
class QuizBrain:
	""" Its constructor Wait for a list and that list must contain a dictionary """
	def __init__(self, question_list: list) -> None:
		self.question_number:int = 0
		self.question_list:list = question_list
		self.score:int = 0

	def still_has_question(self) -> bool:
		return self.question_number < len(self.question_list)
	
	def next_cuestion(self) -> str:
		self.current_question = self.question_list[self.question_number]
		self.question_number+=1
		q_text = html.unescape(self.current_question.text)

		return f"Q.{self.question_number}: {q_text}"

	def check_answer(self, user_answer:str)-> bool:
		current_answer = self.current_question.answer
		if user_answer.lower() == current_answer.lower():
			self.score+=1
			return True
		else:
			return False
