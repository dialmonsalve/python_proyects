from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
hlep = "Hello"

for question in question_data:

	text = question["text"]
	answer = question["answer"]

	new_question = Question(text, answer)

	question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while (quiz.still_has_question()):
	quiz.next_cuestion()

print("You've complete the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

