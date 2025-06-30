from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

LEFT_POSITION = (-350, 0)
RIGHT_POSITION = (350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("🏓🏓🏓 Pong 🏓🏓🏓")
screen.tracer(0)

left_paddle = Paddle(LEFT_POSITION)
right_paddle = Paddle(RIGHT_POSITION)
ball = Ball()
score = Score()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.update_left_score()

    if ball.xcor() < -380:
        ball.reset_position()
        score.update_right_score()

screen.exitonclick()