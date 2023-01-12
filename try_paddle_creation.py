from turtle import Turtle
class PaddleCreation(Turtle):
    def __init__(self):
        super().__init__()
        self.paddles=[]
        for i in range(2):
            tim=Turtle()
            tim.penup()
            tim.shape("square")
            tim.speed("fastest")
            tim.setheading(90)
            tim.shapesize(stretch_len=5,stretch_wid=1)
            tim.color("white")
            self.paddles.append(tim)

        self.paddles[0].goto(x=350,y=0)
        self.paddles[1].goto(x=-350,y=0)
