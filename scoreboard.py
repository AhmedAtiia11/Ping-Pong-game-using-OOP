from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score=0
        self.left_score=0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,180)
        self.score()

    def score(self):
        self.write(f"{self.left_score}   {self.right_score}",align="center",font=("Courier",80,"normal"))


    def update_left(self):
        self.left_score+=1
        self.clear()
        self.score()

    def update_right(self):
        self.right_score+=1
        self.clear()
        self.score()