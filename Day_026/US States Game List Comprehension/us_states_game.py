import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

guessed_states = []
total_states = 50

is_game_on = True
while is_game_on:
    answer = screen.textinput(title=f"{len(guessed_states)}/{total_states} Guessed Correct", prompt="What is another state's name?").capitalize()
    if answer == 'Exit' or len(all_states) == 0:
        is_game_on = False
    elif answer in all_states:
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        state_data = data[data["state"] == answer]
        tim.goto(state_data.x.item(), state_data.y.item())
        tim.write(answer)
        guessed_states.append(answer)

states_to_learn = [state for state in all_states if state not in guessed_states]

df = pandas.DataFrame(states_to_learn)
df.to_csv('states_to_learn.csv')