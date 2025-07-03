import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

guessed_states = []
total_states = 50

is_game_on = True
while is_game_on:
    answer = screen.textinput(title=f"{len(guessed_states)}/{total_states} Guessed Correct", prompt="What is another state's name?").capitalize()
    if answer == 'Exit' or len(states) == 0:
        is_game_on = False
    elif answer in states:
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        state_data = data[data["state"] == answer]
        tim.goto(state_data.x.item(), state_data.y.item())
        tim.write(answer)
        states.remove(answer)

df = pandas.DataFrame(states)
df.to_csv('states_to_learn.csv')
