from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.points = 0
        self.update_score()

    def add_points(self):
        self.points += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.goto(0, 260)
        self.color("white")
        self.write(f"Score: {self.points}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.clear()
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)
        self.goto(0, -20)
        self.write(f"Final Score: {self.points}", False, ALIGNMENT, ("Courier", 15, "italic"))





