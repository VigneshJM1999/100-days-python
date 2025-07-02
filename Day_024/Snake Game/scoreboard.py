from turtle import Turtle

FONT = ('Arial', 12, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.save_high_score()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def get_high_score(self):
        with open('score.txt', 'r') as file:
            score = int(file.read())
            return score

    def save_high_score(self):
        with open('score.txt', 'w') as file:
            file.write(f"{self.high_score}")
