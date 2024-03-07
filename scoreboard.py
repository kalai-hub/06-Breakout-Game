# scoreboard.py
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-330, 270)
        self.write(f"Score:{self.score}", align="center", font=("Courier", 20, "normal"))

    def point(self):
        self.score += 1
        self.update_score()

    def point_reduce(self):
        if self.score == 0:
            pass
        else:
            self.score -= 1
            self.update_score()

