from turtle import Screen, Turtle

s = Screen()
s.setup(width=800, height=600)
s.bgcolor("black")

t = Turtle()
t.shape("square")
t.color("white")
t.penup()
t.shapesize(stretch_wid=5, stretch_len=1)
t.goto(350, 0)

s.exitonclick()
