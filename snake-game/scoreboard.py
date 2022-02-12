# Scoreboard class
# Includes File I/O

from turtle import Turtle

# Usually you don't want hard coded text in your code
ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as h:
            self.high_score = int(h.read())
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(x=0, y=270)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.show_score()

    def try_again(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as h:
                h.write(f"{self.score}")
            self.high_score = self.score
        # Setting the score back to 0
        self.score = 0
        self.show_score()
