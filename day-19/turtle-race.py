import random
import turtle as t

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtl will win the race? enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
print(user_bet)
y = -150

for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-220, y)
    all_turtles.append(new_turtle)
    y += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
