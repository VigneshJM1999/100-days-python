from turtle import Turtle

class Bricks(Turtle):

    def __init__(self):
        super().__init__()
        self.brick_width = 50
        self.brick_height = 20
        self.brick_spacing = 5
        self.start_x = -360
        self.start_y = 260
        self.brick_colors = ["red", "orange", "yellow", "green", "blue"]
        self.num_rows = len(self.brick_colors)
        self.num_cols = 13
        self.bricks = self.create_bricks()

    def draw_bricks(self, x, y, color):
        brick = Turtle("square")
        brick.penup()
        brick.color(color)
        brick.shapesize(stretch_wid=self.brick_height / 20, stretch_len=self.brick_width / 20)
        brick.goto(x + self.brick_width / 2, y - self.brick_height / 2)  # center correction
        return brick

    def create_bricks(self):
        bricks = []
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                x = self.start_x + col * (self.brick_width + self.brick_spacing)
                y = self.start_y - row * (self.brick_height + self.brick_spacing)
                color_index = row % len(self.brick_colors)
                brick = self.draw_bricks(x, y, self.brick_colors[color_index])
                bricks.append(brick)
        return bricks
