from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("orange")
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 250)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)

    def update_left_score(self):
        self.left_score += 1
        self.display_score()

    def update_right_score(self):
        self.right_score += 1
        self.display_score()
