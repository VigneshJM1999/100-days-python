import turtle as t
import random

color_list = [(199, 162, 100), (62, 91, 128), (140, 170, 192), (139, 90, 48), (219, 206, 119), (135, 27, 52)]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

def starting_position():
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)

def move_to_start():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

def draw_painting():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

starting_position()

for i in range(10):
    tim.penup()
    draw_painting()
    move_to_start()

screen = t.Screen()
screen.exitonclick()
