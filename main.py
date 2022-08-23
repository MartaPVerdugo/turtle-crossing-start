import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
screen.listen()
screen.bgcolor("black")
screen.title("Turtle Crossing Game")
screen.onkey(player.move, "Up")
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    # detect collision with a car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect player has reached the other side
    if player.ycor() > 250:
        scoreboard.increase_level()
        scoreboard.update_level()
        player.go_to_start()
        cars.level_up()




screen.exitonclick()
