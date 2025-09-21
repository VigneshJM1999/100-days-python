from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.position = (0, -260)
        self.create_paddle(self.position)

    def create_paddle(self, position):
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("brown")
        self.goto(position)

    def go_right(self, ball=None):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
        if ball and not ball.in_motion:
            ball.follow_paddle(self)

    def go_left(self, ball=None):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
        if ball and not ball.in_motion:
            ball.follow_paddle(self)
