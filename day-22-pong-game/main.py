import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

s = Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.title("Pong")
s.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
sb = Scoreboard()

s.listen()
s.onkey(r_paddle.go_up, "Up")
s.onkey(r_paddle.go_down, "Down")
s.onkey(l_paddle.go_up, "w")
s.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()

    # detect collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect when right paddle misses
    if ball.xcor() > 380:
        print("ball out of bounds")
        ball.reset_position()
        sb.l_point()

    # detect when left paddle misses
    if ball.xcor() < -380:
        print("ball out of bounds")
        ball.reset_position()
        sb.r_point()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        print("made contact")
        ball.bounce_x()

s.exitonclick()
