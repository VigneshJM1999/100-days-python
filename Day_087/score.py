from turtle import Turtle

FONT = ('Arial', 12, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def update_score(self, score):
        self.clear()
        self.score += score
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align="center", font=('Arial', 24, 'normal'))

    def you_win(self):
        self.goto(0, 0)
        self.color("green")
        self.write("YOU WIN!", align="center", font=('Arial', 24, 'normal'))

    def you_lose(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align="center", font=('Arial', 24, 'normal'))
