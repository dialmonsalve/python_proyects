from tkinter import Tk, Label, Button, Entry

class LabelClass():

	def __init__(self,row, column, text) -> None:

		label = Label(text=text)

		label.grid(row=row, column=column)

def calculate_km():

	conv = round(float(my_entry.get()) * 1.609, 1)

	lbl_calculate = LabelClass(row=1, column=1, text=conv)

	print(conv)

root = Tk()
root.title("Mile to Km Converter")
root.minsize(width=300, height=100)
root.maxsize(width=300, height=100)
root.config(padx=10, pady=10)

lbl_is_equal_to = LabelClass(row=1,column=0, text="Is equal to")
lbl_miles = LabelClass(row=0, column=2 ,text="Miles")
lbl_km = LabelClass(row=1, column=2, text="Km")

my_entry = Entry()
my_entry.grid(row=0, column=1)

btn_calculate = Button(text="Calculate")
btn_calculate.grid(row=2, column=1)
btn_calculate.config(command=calculate_km)

root.mainloop()