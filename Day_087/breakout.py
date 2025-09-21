from turtle import Screen
from paddle import Paddle
from ball import Ball
from lives import Lives
from bricks import Bricks
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")

paddle = Paddle()
ball = Ball()
lives = Lives()
score = Score()
bricks = Bricks().bricks

screen.tracer(0)
screen.listen()

screen.onkey(lambda: paddle.go_right(ball), "Right")
screen.onkey(lambda: paddle.go_left(ball), "Left")
screen.onkey(lambda: paddle.go_right(ball), "d")
screen.onkey(lambda: paddle.go_left(ball), "a")

screen.onkey(ball.launch, "Up")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(paddle) < 60 and ball.ycor() < -240:
        ball.bounce_y()

    if ball.ycor() < -280:
        lives.update_lives()
        ball.reset_position()

        if lives.lives_left == 0:
            score.you_lose()
            is_game_on = False

    for brick in bricks:
        if ball.distance(brick) < 30:
            ball.bounce_y()
            brick.hideturtle()
            bricks.remove(brick)
            score.update_score(10)
            break

    if len(bricks) == 0:
        score.you_win()
        is_game_on = False

screen.exitonclick()
