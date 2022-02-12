# Paddle class

from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coords):
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(coords)
        self.shape("square")
        self.color("white")

    def move_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), y=new_y)
