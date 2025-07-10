from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
chosen_word = {}
word_list = []

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    word_list = original_data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")

def update_card():
    global chosen_word, flip_timer
    window.after_cancel(flip_timer)
    chosen_word = random.choice(word_list)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=chosen_word["French"], fill="black")
    canvas.itemconfig(flash_card, image=front_card_image)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=chosen_word["English"], fill="white")
    canvas.itemconfig(flash_card, image=back_card_image)

def known_word():
    word_list.remove(chosen_word)
    pandas.DataFrame(word_list).to_csv("data/words_to_learn.csv", index=False)
    update_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(0, lambda: None)

canvas = Canvas(width=800, height=526)
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
flash_card = canvas.create_image(400, 263, image=front_card_image)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=update_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=known_word)
right_button.grid(column=1, row=1)

update_card()
window.mainloop()
