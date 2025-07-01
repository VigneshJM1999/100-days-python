import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("🐢 Crossing Game 🕹️")
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_turtle, "Up")

game_is_on = True
loop = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if player.distance(car) < 27:
            game_is_on = False
            score.game_over()

    if player.at_finish_line():
        score.add_level()
        player.move_to_start()
        car_manager.increase_speed()

screen.exitonclick()
