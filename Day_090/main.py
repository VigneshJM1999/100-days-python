import tkinter as tk

class DisappearingTextApp:
    def __init__(self, master):
        self.master = master
        master.title("Disappearing Text App")

        self.text_area = tk.Text(master, wrap="word", width=50, height=20)
        self.text_area.pack(pady=10)
        self.text_area.bind("<Key>", self.reset_timer)

        self.timer_id = None
        self.inactivity_timeout = 5000 # milliseconds (5 seconds)

        self.reset_timer() # Start the timer initially

    def reset_timer(self, event=None):
        if self.timer_id:
            self.master.after_cancel(self.timer_id)
        self.timer_id = self.master.after(self.inactivity_timeout, self.clear_text)

    def clear_text(self):
        self.text_area.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = DisappearingTextApp(root)
    root.mainloop()