# Keanu Aloua
# Day 20 and Day 21
# December 20, 2021
# Finished December 21, 2021
# December 23, 2021 EDIT -Making a snake game with use of File I/O

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creating snake object
snake = Snake()
food = Food()
user_score = Scoreboard()

# Screen will listen for commands by user
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Program start
game_start = True
while game_start:
    screen.update()
    time.sleep(0.08)  # Lets the snake move all together
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.rand_location()
        user_score.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -295 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        user_score.try_again()
        snake.reset()

    # Detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            user_score.try_again()
            snake.reset()

# Exit program
screen.exitonclick()
