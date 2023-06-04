from turtle import Turtle

SCORE = 0
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(f"Score : {SCORE}")

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over")

    def score(self):
        global SCORE
        SCORE += 1
        self.clear()
        self.write(f"Score : {SCORE}")