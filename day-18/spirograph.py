import random
import turtle as t

timmy = t.Turtle()
timmy.speed("fastest")
t.colormode(255)


def get_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tup = (r, g, b)
    return my_tup


for _ in range(int(360 / 10)):
    timmy.pencolor(get_color())
    timmy.circle(100)
    timmy.left(10)

screen = t.Screen()
screen.exitonclick()
