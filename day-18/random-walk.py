import random
import turtle as t

tee = t.Turtle()
t.width(15)
t.speed(10)
t.colormode(255)

colors = [
    "cornflower blue", "cyan", "light sea green", "lime green", "chartreuse",
    "olive", "tan", "firebrick", "tomato", "purple", "slate blue"
]

directions = [0, 90, 180, 270]


def get_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tup = (r, g, b)
    return my_tup


# _ when you're not going to use the iterator
for _ in range(200):
    t.pencolor(get_color())
    t.forward(30)
    t.setheading((random.choice(directions)))
