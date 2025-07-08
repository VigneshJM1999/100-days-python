from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) != 0 and len(password) != 0:
        is_ok = messagebox.askokcancel(title=f"🌐 {website} 🌐",
                                       message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n"
                                               f"Is it okay to save?")

        if is_ok:
            with open("password.txt", 'a') as file:
                file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showinfo(title="⚠️⚠️⚠️", message="Please fill out all fields.")

def password_generator():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []
    nr_letters = randint(8, 10)
    nr_numbers = randint(2, 4)
    nr_symbols = randint(2, 4)

    password_letters = [choice(letters) for i in range(nr_letters)]
    password_numbers = [choice(numbers) for i in range(nr_numbers)]
    password_symbols = [choice(symbols) for i in range(nr_symbols)]

    password = password_letters + password_numbers + password_symbols

    shuffle(password)

    final_password = ''.join(password)
    password_entry.insert(0, final_password)
    pyperclip.copy(final_password)


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/ Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky='w')
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky='w')
email_entry.insert(0, "vignesh@vignesh.com")

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3, sticky='w')

password_generate = Button(text="Generate Password", command=password_generator)
password_generate.grid(column=2, row=3, sticky='w')

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
