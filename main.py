from turtle import Turtle,Screen
from paddle import Paddle
from paddle_ball import PaddleBall
from scoreboard import ScoreBoard
import time
screen=Screen()
screen.bgcolor("black")
screen.title("Ping Pong")
screen.setup(width=800,height=600)
screen.tracer(0)
screen.listen()

def right_up():
    r_paddle.forward(20)
def right_down():
    r_paddle.backward(20)   
def left_up():
    l_paddle.forward(20)
def left_down():
    l_paddle.backward(20)  
# tim=Turtle()
# tim.penup()
# tim.shape("square")
# tim.speed("fastest")
# tim.setheading(90)
# tim.shapesize(stretch_len=5,stretch_wid=1)
# tim.color("white")
# tim.goto(x=-350,y=0)

# rocket=PaddleCrea=tion()
# r_paddle=rocket.paddles[0]
# l_paddle=rocket.paddles[1]
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=PaddleBall()
score=ScoreBoard()

# ball=Paddle.paddle_ball()
screen.onkey(right_up,"Up")
screen.onkey(right_down,"Down")

screen.onkey(left_up,"w")
screen.onkey(left_down,"s")
y_reverse=1
x_reverse=1
while True:
    screen.update()
    time.sleep(.1)
    ball.move(y_reverse,x_reverse)
    if (ball.ycor() > 280) or (ball.ycor()<-280):
        y_reverse*=-1
    if ball.distance(r_paddle) < 50 and ball.xcor() >320:
        x_reverse*=-1
    if ball.distance(l_paddle) < 50 and ball.xcor() <-320:
        x_reverse*=-1
    if ball.xcor()>370:
        score.update_left()
        ball.position_reset()
        x_reverse=-1

    if ball.xcor()<-370:
        score.update_right()
        ball.position_reset()
        x_reverse=1


        
     
    

    

screen.exitonclick()
