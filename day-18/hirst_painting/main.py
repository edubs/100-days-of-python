# colors = colorgram.extract('painting.jpg', 30)
# rgb_colors = []
#
#
# def extract_values(color_object):
#     tuppy = (color_object.rgb[0], color_object.rgb[1], color_object.rgb[2])
#     return tuppy
#
#
# for c in range(len(colors)):
#     rgb_colors.append(extract_values(colors[c]))
#
# print(rgb_colors)

import random
import turtle as t

timmy = t.Turtle()
timmy.speed("fastest")
t.colormode(255)
y = 0

color_list = [(229, 130, 63), (157, 97, 26), (19, 36, 56), (43, 106, 150), (239, 79, 93), (224, 212, 1),
              (232, 240, 236), (148, 184, 220), (211, 153, 162), (130, 215, 207), (237, 97, 31), (165, 46, 136),
              (85, 183, 5), (52, 91, 86), (133, 217, 220), (226, 205, 85), (214, 133, 23), (137, 192, 167),
              (212, 184, 174), (229, 169, 180), (162, 191, 224), (46, 75, 71), (88, 137, 163), (16, 70, 115),
              (34, 47, 46), (121, 37, 99), (104, 129, 154)]


def draw_line():
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()


def move_up():
    timmy.penup()
    timmy.left(90)
    timmy.forward(50)
    global y
    y += 50
    timmy.goto(0, y)
    timmy.right(90)
    timmy.pendown()


for _ in range(10):
    draw_line()
    move_up()

screen = t.Screen()
screen.exitonclick()
