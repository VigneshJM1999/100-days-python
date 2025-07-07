import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

count = 0
timer = None

def count_down(time):
    minutes = math.floor(time / 60)
    seconds = int(time % 60)
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if time > 0:
        global timer
        timer = window.after(1000, count_down, time - 1)
    else:
        start_timer()
        check_marks = ""
        for i in range(int(math.floor(count/2))):
            check_marks += "✔"
        status_symbol.config(text=check_marks)

def start_timer():
    global count
    count += 1

    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if count % 8 == 0:
        count_down(long_break)
        title_label.config(text="Long Break", fg=RED)
    elif count % 2 == 0:
        count_down(short_break)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work)
        title_label.config(text="Work", fg=GREEN)

def reset_timer():
    global count
    count = 0
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    status_symbol.config(text="")

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
title_label.grid(column=1, row=0)

canvas = Canvas(width=206, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_image)
timer_text = canvas.create_text(103, 133, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

status_symbol = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
status_symbol.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
