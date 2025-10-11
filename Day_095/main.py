import turtle
import math
import random
import time

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

alien_shape = ((0, 15), (-15, 0), (-5, 0), (-5, -5), (5, -5), (5, 0), (15, 0))
screen.register_shape("alien", alien_shape)

player_shape = ((0, 15), (-15, -15), (15, -15))
screen.register_shape("player", player_shape)

game_state = "playing"

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-350, -250)
border_pen.pendown()
border_pen.pensize(3)
for side in range(2):
    border_pen.fd(700)
    border_pen.lt(90)
    border_pen.fd(500)
    border_pen.lt(90)
border_pen.hideturtle()

score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-340, 260)
score_string = "Score: %s" % score
score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

player = turtle.Turtle()
player.color("cyan")
player.shape("player")
player.penup()
player.speed(0)
player.setposition(0, -225)
player.setheading(90)
player_speed = 20

laser = turtle.Turtle()
laser.color("yellow")
laser.shape("triangle")
laser.shapesize(0.3, 0.3)
laser.penup()
laser.speed(0)
laser.setheading(90)
laser.hideturtle()
laser_speed = 30
laser_state = "ready"

aliens = []
num_aliens = 24
alien_start_x = -225
alien_start_y = 175
alien_speed = 2

for i in range(num_aliens):
    alien = turtle.Turtle()
    alien.color("red")
    alien.shape("alien")
    alien.penup()
    alien.speed(0)
    x = alien_start_x + (75 * (i % 8))
    y = alien_start_y - (50 * (i // 8))
    alien.setposition(x, y)
    aliens.append(alien)

barriers = []
barrier_start_x = -250
barrier_y = -150
for i in range(4):
    for j in range(10): # Each barrier is made of smaller blocks
        barrier = turtle.Turtle()
        barrier.shape("square")
        barrier.shapesize(0.5, 0.5)
        barrier.color("green")
        barrier.penup()
        barrier.speed(0)
        x = barrier_start_x + (i * 170) + (j % 5 * 10)
        y = barrier_y - (j // 5 * 10)
        barrier.setposition(x, y)
        barriers.append(barrier)

def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -330:
        x = -330
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 330:
        x = 330
    player.setx(x)

def fire_laser():
    global laser_state
    if laser_state == "ready":
        laser_state = "fire"
        x = player.xcor()
        y = player.ycor() + 20
        laser.setposition(x, y)
        laser.showturtle()

def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    return distance < 20

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(fire_laser, "space")

while game_state == "playing":
    screen.update()
    time.sleep(0.01)

    for alien in aliens:
        x = alien.xcor()
        x += alien_speed
        alien.setx(x)

        if alien.xcor() > 330 or alien.xcor() < -330:
            for a in aliens:
                y = a.ycor()
                y -= 40
                a.sety(y)
                alien_speed *= -1
                break
        if is_collision(laser, alien):
            laser.hideturtle()
            laser_state = "ready"
            laser.setposition(0, -400)
            alien.hideturtle()
            aliens.remove(alien)
            score += 10
            score_string = "Score: %s" % score
            score_pen.clear()
            score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))

        if is_collision(alien, player):
            player.hideturtle()
            alien.hideturtle()
            game_state = "gameover"
            break

        if alien.ycor() < -225:
            game_state = "gameover"
            break

    if laser_state == "fire":
        y = laser.ycor()
        y += laser_speed
        laser.sety(y)

    if laser.ycor() > 275:
        laser.hideturtle()
        laser_state = "ready"

    for barrier in barriers:
        if laser.isvisible() and is_collision(laser, barrier):
            laser.hideturtle()
            laser_state = "ready"
            laser.setposition(0, -400)
            barrier.hideturtle()
            barriers.remove(barrier)
            break

    for alien in aliens:
        for barrier in barriers:
            if is_collision(alien, barrier):
                barrier.hideturtle()
                barriers.remove(barrier)
                break

    if not aliens:
        game_state = "win"

final_message_pen = turtle.Turtle()
final_message_pen.speed(0)
final_message_pen.color("white")
final_message_pen.penup()
final_message_pen.hideturtle()

if game_state == "gameover":
    final_message_pen.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
elif game_state == "win":
    final_message_pen.write("YOU WIN!", align="center", font=("Arial", 24, "bold"))

screen.mainloop()
