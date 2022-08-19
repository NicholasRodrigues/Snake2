from turtle import Turtle

import self as self

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.points = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.scores_list = []
        self.name_list = []
        self.update_score()

    def add_points(self):
        self.points += 1
        self.update_score()

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.points = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.color("white")
        self.write(f"Score: {self.points} High Score: {self.high_score}", False, ALIGNMENT, FONT)



