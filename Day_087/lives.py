from turtle import Turtle

ALIGNMENT = "left"
FONT = ('Arial', 12, 'normal')

class Lives(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("orange")
        self.lives_left = 3
        self.hideturtle()
        self.display_lives()

    def display_lives(self):
        self.clear()
        self.goto(-380, 270)
        self.write(f"Lives Left: {self.lives_left}", align=ALIGNMENT, font=FONT)

    def update_lives(self):
        self.lives_left -= 1
        self.display_lives()
