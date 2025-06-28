from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make you bet.", prompt="Which turtle will cross the line first? Choose a color")
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
y_position = [-160, -100, -40, 20, 80, 140]

turtles = []
if user_choice:
    is_race_on = True
    for i in range(len(colors)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[i])
        new_turtle.goto(-240, y_position[i])
        turtles.append(new_turtle)


while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 220:
            winner = turtle.pencolor()
            is_race_on = False
            if user_choice == winner:
                print(f"🎉 You have won the bet! {winner.capitalize()} is the winning color!")
            else:
                print(f"😭 You have lost the bet! {winner.capitalize()} is the winning color!")
        else:
            forward_distance = random.randint(0, 10)
            turtle.forward(forward_distance)

screen.exitonclick()
