from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.move_distance = STARTING_MOVE_DISTANCE
        self.all_cars = []
        self.create_car()

    def create_car(self):
        if len(self.all_cars) < 20:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=3)
            new_car.goto(280, random.randint(-240, 280))
            self.all_cars.append(new_car)
        else:
            pass

    def drive(self):
        for car in self.all_cars:
            if car.xcor() < -300:
                self.all_cars.pop(car)
            else:
                new_x = car.xcor() - self.move_distance
                car.goto(new_x, car.ycor())

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT
