from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 15, "normal")
SCOREBOARD_Y_POS = 270
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, SCOREBOARD_Y_POS)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, SCOREBOARD_Y_POS-10)
        self.write(f"SCORE = {self.score}", True, ALIGNMENT, FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align =ALIGNMENT, font=FONT)
    def add_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_scoreboard()
