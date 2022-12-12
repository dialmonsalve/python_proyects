from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
word = {}
data_dict={}

try:
	data = pandas.read_csv("12_flash-card-project/data/words_to_learn.cvs")
except FileNotFoundError:
	original_data = pandas.read_csv("12_flash-card-project/data/english_words.cvs")
	data_dict = original_data.to_dict(orient="records")
else:
	data_dict = data.to_dict(orient="records")


def random_word():
	global word, flip_timer
	root.after_cancel(flip_timer)
	word = choice(data_dict)
	canvas.itemconfig(canvas_title, text="English", fill="black")
	canvas.itemconfig(canvas_text, text=word["en"], fill="black")
	canvas.itemconfig(card_background, image=card_front_img)
	flip_timer = root.after(3000, func=flip_card)
	
def flip_card():
	canvas.itemconfig(canvas_title, text="Español", fill="#fff")
	canvas.itemconfig(canvas_text, text=word["es"], fill="#fff")
	canvas.itemconfig(card_background, image=card_back_img)

def is_known():
	data_dict.remove(word)
	data = pandas.DataFrame(data_dict, index=False)
	data.to_csv("12_flash-card-project/data/words_to_learn.cvs")
	random_word()

root = Tk()
root.title("Flash cards")
root.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = root.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="12_flash-card-project/images/card_front.png")
card_back_img = PhotoImage(file="12_flash-card-project/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
canvas_text = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

img_right = PhotoImage(file="12_flash-card-project/images/right.png")
right = Button(image=img_right, highlightthickness=0, command=is_known)
right.grid(row=1, column=0)

img_wrong = PhotoImage(file="12_flash-card-project/images/wrong.png")
wrong = Button(image=img_wrong, highlightthickness=0, command=random_word)
wrong.grid(row=1, column=1)

random_word()


root.mainloop()