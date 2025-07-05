from tkinter import *

def calculate_kilometer():
    miles = entry.get()
    answer = int(miles) * 1.609
    kilometer.config(text=f"{answer}")

window = Tk()

window.title("Miles To Kilometer Converter")

label_1 = Label(text="equal to")
label_1.grid(column=0, row=1)
label_1.config(padx=5, pady=5)

entry = Entry(width=10)
entry.grid(column=1, row=0)

kilometer = Label(text="0")
kilometer.grid(column=1, row=1)
kilometer.config(padx=5, pady=5)

calculate = Button(text="Calculate", command=calculate_kilometer)
calculate.grid(column=1, row=2)
calculate.config(padx=5, pady=5)

label_2 = Label(text="Miles")
label_2.grid(column=2, row=0)
label_2.config(padx=5, pady=5)

label_3 = Label(text="Km")
label_3.grid(column=2, row=1)
label_3.config(padx=5, pady=5)

window.mainloop()
