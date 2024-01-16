import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.all_cars = []
        self.create_car()

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, random.randint(-230, 230))
            self.all_cars.append(new_car)

    def drive(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.move_distance
            car.goto(new_x, car.ycor())

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT
