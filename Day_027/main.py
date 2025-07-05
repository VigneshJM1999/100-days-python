from tkinter import *

window = Tk()

window.title("My First GUI Program.")
window.minsize(width=500, height=300)

my_label = Label(text="This is a text.", font=("Ariel", 24, "italic"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click me!", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click me!", command=button_clicked)
new_button.grid(column=2, row=0)

input = Entry(width=15)
input.grid(column=3, row=2)


window.mainloop()
