import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

s = Screen()
s.setup(width=600, height=600)
s.tracer(0)

p = Player()
s.listen()
s.onkey(p.move_up, "Up")
c = CarManager()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    s.update()
    c.drive()

    # detect crossing the finish line
    if p.ycor() > 280:
        p.level_up()

s.exitonclick()
