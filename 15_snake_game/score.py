from turtle import Turtle
from pathlib import Path

ALIGNMENT="center"
FONT=("Courier", 18, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        file_path = Path(__file__).parent / "data.txt"
        with open(file_path) as data: 
            self.high_score = int(data.read())
        self.color("White")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file_path = Path(__file__).parent / "data.txt"
            with open(file_path, mode="w") as data:
                 data.write(f"{self.high_score}") 
        self.score = 0
        self.update()

    def inc_score(self):
            self.score += 1
            self.update()
    