# Snake Class

from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

starting_positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("green")
        segment.penup()
        segment.goto(position)
        self.snake.append(segment)

    def reset(self):
        # Resets the snake to the middle
        for segs in self.snake:
            segs.goto(1000, 1000)
        self.snake.clear()  # Clears all items in the list
        self.create_snake()
        self.head = self.snake[0]

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for seg in range(len(self.snake) - 1, 0, -1):
            # Second to last segment
            new_x = self.snake[seg - 1].xcor()
            new_y = self.snake[seg - 1].ycor()

            # Last segment goes to location of the segment in front
            self.snake[seg].goto(new_x, new_y)
        self.snake[0].forward(20)

    def up(self):
        # If the heading is going down, then snake can not go up
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # If the heading is going up, then snake can not go down
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        # If the heading is going left, then snake can not go right
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        # If the heading is going right, then snake can not go left
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
