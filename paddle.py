from turtle import Turtle
class  Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.setheading(90)
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.goto(position)

 