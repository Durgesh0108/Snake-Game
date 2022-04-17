from turtle import Turtle

ALIGNMENT = "Center"
FONT = ["courier", 15, "bold"]


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.color("red")
        self.hideturtle()
        self.clear()
        self.write(f"Game Over. You Scored: {self.score}", False, align= ALIGNMENT, font= FONT)


