import random
from turtle import Turtle, Screen

screen = Screen()
bob = Turtle()
shapes = [3, 4, 5, 6, 7, 8, 9, 10]

valid_pencolors = [
    "black", "red", "green", "blue", "yellow", "orange", "purple",
    "brown", "pink", "gray", "cyan", "magenta", "violet", "indigo", "turquoise",
    "olive", "maroon", "navy", "teal", "salmon", "lime", "gold", "silver", "coral",
    "lavender", "peach", "plum", "sienna", "thistle", "orchid",
    "mint", "aqua", "chartreuse",
]


def draw_side(sides):
    angle = 360 / sides
    bob.pencolor(random.choice(valid_pencolors))

    for r in range(sides):
        bob.forward(100)
        bob.right(angle)


for s in shapes:
    draw_side(s)

screen.exitonclick()
