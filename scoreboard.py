from turtle import Turtle , Screen

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score_r = 0
        self.score_l = 0
        self.penup()
        self.goto(0, 260)
        self.write(f"{self.score_l} | SCORE | {self.score_r} ", align='center', font=('Arial', 24, 'normal'))
        self.ht()

    def score_increase_r(self):
        self.clear()
        self.score_r += 1
        self.write(f"{self.score_l} | SCORE | {self.score_r} ", align='center', font=('Arial', 24, 'normal'))

    def score_increase_l(self):
        self.clear()
        self.score_l += 1
        self.write(f"{self.score_l} | SCORE | {self.score_r} ", align='center', font=('Arial', 24, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=('Arial', 24, 'bold'))
        self.goto(0,-60)
        self.write(f"  {self.score_l} | SCORE | {self.score_r} ", align='center', font=('Arial', 26, 'normal'))