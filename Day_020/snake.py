from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
FORWARD_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for i in range(3):
            snake = Turtle(shape="square")
            snake.penup()
            snake.color("white")
            snake.goto(STARTING_POSITIONS[i])
            self.snakes.append(snake)
        return

    def move_snake(self):
        for snake in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake - 1].xcor()
            new_y = self.snakes[snake - 1].ycor()
            self.snakes[snake].goto(new_x, new_y)
        self.head.forward(FORWARD_DISTANCE)
        return

    def move_up(self):
        if self.head.heading() != DOWN:
            self.snakes[0].setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.snakes[0].setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.snakes[0].setheading(RIGHT)



