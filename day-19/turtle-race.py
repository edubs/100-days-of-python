from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtl will win the race? enter a color: ")
print(user_bet)
timmy = Turtle()


screen.exitonclick()
