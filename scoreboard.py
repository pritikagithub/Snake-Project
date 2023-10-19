from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.increase_score()

    def increase_score(self):
        self.write(arg = f"Score : {self.score}", align = "center", font = ("Century Schoolbook", 12, "italic"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.increase_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg = f"!! GAME OVER !!", align="center", font = ("Courier", 15, "bold"))