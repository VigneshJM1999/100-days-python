from turtle import Turtle

FONT = ("Courier", 15, "normal")
POSITION = (-260, 260)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.level = 1
        self.hideturtle()
        self.goto(POSITION)
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def add_level(self):
        self.level += 1
        self.display_level()

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("🛑 GAME OVER 🛑", align="center", font=FONT)

