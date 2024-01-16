import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
car_manager = CarManager()
player = Player()
screen.onkey(player.move_up, "Up")

game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.drive()

    # detect crossing the finish line
    if player.is_at_finish_line():
        player.reset_position()
        scoreboard.level_clear()
        car_manager.speed_up()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
