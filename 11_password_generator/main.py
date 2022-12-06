from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():

	entry_password.delete(0, END)

	password_list = []

	password_letter = [choice(letters) for _ in range(randint(8, 10))]
	password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
	password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

	password_list = password_letter + password_symbols +password_numbers

	shuffle(password_list)

	password = "".join(password_list)

	entry_password.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

		website = entry_website.get()
		email = entry_username.get()
		password = entry_password.get()

		new_data = {
			website:{
				"email": email,
				"password" : password
			}
		}

		if website == "" or email == "" or password == "":
			messagebox.showinfo(title="title", message="All fields must be information")

			return
		
		is_ok = messagebox.askokcancel(title=website, message=f"These are the detail entered: \n{email}\n password: {password}\n Is it ok to save?")

		if is_ok:
			try:
				with open("11_password_generator/data.json", "r") as data_file:
					data = json.load(data_file)
					data.update(new_data)
			except FileNotFoundError:
				
				with open("11_password_generator/data.json", "w") as data_file:
					json.dump(new_data, data_file, indent=4)
			else:
				with open("11_password_generator/data.json", "w") as data_file:
					json.dump(data, data_file, indent=4)
			
			finally:
					entry_website.delete(0, END)
					entry_username.delete(0, END)
					entry_password.delete(0, END)
					entry_website.focus()

# ---------------------------- SEARCH DATA ------------------------------- #

def search():

	try:
		with open("11_password_generator/data.json", "r") as data_file:
			data = json.load(data_file)
	except FileNotFoundError:
		messagebox.showinfo(title="Error", message="Data doesn't exist")

	else:
		for website, value in data.items():
			if website == entry_website.get():
				messagebox.showinfo(title=website, message=f"Email:{value['email']}\n\nPassword: {value['password']}")
				return
			else:
				messagebox.showinfo(title="Try again", message=f"No details for {entry_website.get()}")

# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file="11_password_generator/logo.png")
canvas.create_image(100,100, image=padlock_img)
canvas.grid(row=0, column=1)

lbl_website = Label(text="Website")
lbl_website.grid(row=1, column=0)

lbl_username = Label(text="Email/UserName")
lbl_username.grid(row=2, column=0)

lbl_password = Label(text="Password")
lbl_password.grid(row=3, column=0)

entry_website = Entry()
entry_website.config(width=21)
entry_website.grid(row=1, column=1,  sticky="EW")
entry_website.focus()

entry_username = Entry()
entry_username.config(width=35)
entry_username.grid(row=2, column=1, columnspan=2, sticky="EW")

entry_password = Entry()
entry_password.config(width=21)
entry_password.grid(row=3, column=1, sticky="EW")

btn_gen_password = Button(text="Generate Password")
btn_gen_password.config(command=generate_password)
btn_gen_password.grid(row=3, column=2)

btn_gen_password = Button(text="Search")
btn_gen_password.config(command=search)
btn_gen_password.grid(row=1, column=2, sticky="EW")

btn_add = Button(text="Add")
btn_add.config(width=36, command=save)
btn_add.grid(row=4, column=1, columnspan=2, sticky="EW")

root.mainloop()