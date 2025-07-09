from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

def save_password():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if len(website) != 0 and len(password) != 0:
        is_ok = messagebox.askokcancel(title=f"🌐 {website} 🌐",
                                       message=f"These are the details entered:\n"
                                               f"Email: {email}\nPassword: {password}\n\n"
                                               f"Is it okay to save?")
        if is_ok:
            new_data = {
                website: {
                    "email": email,
                    "password": password
                }
            }

            try:
                with open("password.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("password.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("password.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showinfo(title="⚠️ Missing Info", message="Please fill out all fields.")

def search_password():
    website = website_entry.get().strip()
    if not website:
        messagebox.showinfo(title="⚠️ Empty Field", message="Please enter a website to search.")
        return

    try:
        with open("password.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No saved data found.")
        return
    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        pyperclip.copy(password)
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}\n(Password copied!)")
    else:
        messagebox.showinfo(title="Not Found", message=f"No details for '{website}' found.")

def password_generator():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_numbers = randint(2, 4)
    nr_symbols = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]

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

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=2, sticky='ew')
website_entry.focus()

email_entry = Entry(width=33)
email_entry.grid(column=1, row=2, columnspan=2, sticky='ew')
email_entry.insert(0, "vignesh@vignesh.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='ew')

search_button = Button(text="Search", command=search_password, width=13)
search_button.grid(column=2, row=1, sticky='ew')

password_generate = Button(text="Generate Password", command=password_generator)
password_generate.grid(column=2, row=3, sticky='ew')

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

window.mainloop()
