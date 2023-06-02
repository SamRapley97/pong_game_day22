from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Scoreboard class
# Pong class
# Ball class

# Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()

centre_line = Turtle("square")
centre_line.color("white")
centre_line.shapesize(0.5, 1)
centre_line.ht()
centre_line.pu()
centre_line.goto(0, 280)
centre_line.setheading(270)

for _ in range(20):
    centre_line.stamp()
    centre_line.fd(50)

paddy = Paddle()
paddy.goto(360, 0)
paddy.speed("fastest")


computer_paddy = Paddle()
computer_paddy.goto(-360, 0)
paddy.speed("fastest")

screen.listen()

screen.onkey(paddy.up, "Up")
screen.onkey(paddy.down, "Down")

ball = Ball()




game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddy) < 50 and ball.xcor() > 320 or ball.distance(computer_paddy) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()




screen.exitonclick()


