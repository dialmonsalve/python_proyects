import random
from logo import logo

print(logo)
print("Welcome to the number guessing game")
print("I am thinkg of a number between 1 and 100")

level = input("Choose a dificult. Type easy or hard: ").lower()

computer_choice = random.randint(1, 100)
n = 0
flat = True

while flat:

	if (level == "easy"):
		n= 10
		flat=False
	elif (level == "hard"):
		n = 5
		flat=False
	else:
		flat = True
		print("Repeat your election")
		level = input("Choose a dificult. Type easy or hard: ").lower()

print(f"You have {n} attemps to guess the number")

while n:

	user_choice = int(input( "Make a guess " ))

	if (computer_choice > user_choice):
		print("Too low")
		n-=1
	elif (computer_choice < user_choice):
		print("Too high")		
		n-=1
	else:
		print(f"You got it the anser was {computer_choice}")
		break

	print(f"You have {n} attemps to guess the number")
	print("Guess again\n")

	if n == 0:
		print(f"You lose, try again. the number was {computer_choice}\n")
		break

	
