from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.goto(0, -235)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.in_motion = False

    def move(self):
        if self.in_motion:
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)

    def launch(self):
        self.in_motion = True

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.in_motion = False
        self.bounce_x()

    def follow_paddle(self, paddle):
        if not self.in_motion:
            new_x = paddle.xcor()
            self.goto(new_x, -235)
