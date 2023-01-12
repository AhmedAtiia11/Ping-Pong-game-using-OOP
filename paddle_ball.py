from turtle import Turtle
class PaddleBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()


    def move(self,y_reverse,x_reverse): 
        new_x=self.xcor()+(10*x_reverse)
        new_y=self.ycor()+(10*y_reverse)
        self.goto(new_x,new_y)


    def position_reset(self):
        self.goto(0,0)