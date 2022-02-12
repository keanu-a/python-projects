# Keanu Aloua
# December 22, 2021
# Making a pong game

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setting up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Sets up objects
player_1 = Paddle((-350, 0))
player_2 = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Listen for instructions
screen.listen()
screen.onkey(player_1.move_up, "w")
screen.onkey(player_1.move_down, "s")
screen.onkey(player_2.move_up, "Up")
screen.onkey(player_2.move_down, "Down")

# Program start
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -275:
        ball.bounce()

    # Detect collision with a paddle
    if (ball.distance(player_2) < 50 and ball.xcor() > 320) or (ball.distance(player_1) < 50 and ball.xcor() < -320):
        ball.hit()

    # Detects if player misses
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.player_1_point()

    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.player_2_point()

# Exit program
screen.exitonclick()
