from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍🐍🐍 Snake Game 🐍🐍🐍")
screen.tracer(0)
screen.listen()


screen.update()
snake = Snake()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()





screen.exitonclick()
