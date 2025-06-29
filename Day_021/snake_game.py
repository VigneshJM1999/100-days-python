from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍🐍🐍 Snake Game 🐍🐍🐍")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score = Score()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 20:
        food.random_location()
        score.update_score()
        snake.extend_snake()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    for i in snake.snakes[1:]:
        if snake.head.distance(i) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
