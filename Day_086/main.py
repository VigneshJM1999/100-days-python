from tkinter import *
from timeit import default_timer as timer

total_time = 60
start_time = None

def calculate_wpm(text, time_taken):
    words = text.split()
    num_words = len(words)
    minutes = time_taken / 60
    wpm = num_words / minutes if minutes > 0 else 0
    return round(wpm)

def start_test():
    global start_time
    window.destroy()

    test_window = Tk()
    test_window.geometry("600x400")
    test_window.title("Typing Speed Test")

    text_to_type = ("Tkinter is the first option for a lot of learners and developers because it is quick and convenient to use. "
                    "Tkinter is a Python library that can be used to construct basic graphical user interface (GUI) applications. "
                    "In Python, it is the most widely used module for GUI applications.")

    Label(test_window, text="Type the text below:", font=("Arial", 12)).pack(pady=10)
    Label(test_window, text=text_to_type, wraplength=500, font=("Arial", 10)).pack(pady=10)

    entry = Text(test_window, height=5, width=60)
    entry.pack(pady=10)

    result_label = Label(test_window, text="", font=("Arial", 12))
    result_label.pack(pady=10)

    def submit():
        end_time = timer()
        typed_text = entry.get("1.0", END).strip()
        time_taken = end_time - start_time
        wpm = calculate_wpm(typed_text, time_taken)
        result_label.config(text=f"Time Taken: {round(time_taken, 2)}s | WPM: {wpm}")

    Button(test_window, text="Submit", command=submit, bg="blue", fg="white").pack(pady=5)

    start_time = timer()
    test_window.mainloop()

window = Tk()
window.geometry("450x200")
window.title("Typing Speed Test")

Label(window, text="Start the Typing Test", font=("Arial", 14)).pack(pady=40)

Button(window, text="Start", command=start_test, bg="green", fg="white").pack()

window.mainloop()
