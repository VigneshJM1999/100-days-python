from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.move_to_start()

    def move_turtle(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def move_to_start(self):
        self.goto(STARTING_POSITION)
