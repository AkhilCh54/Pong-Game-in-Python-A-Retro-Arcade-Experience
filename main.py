from turtle import Turtle , Screen
from Paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height= 600, width= 800)
screen.bgcolor("black")
screen.tracer(0)
paddle_l = Paddle((-350,0))
paddle_r = Paddle((350,0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(paddle_r.go_up,'Up')
screen.onkey(paddle_r.go_down,'Down')
screen.onkey(paddle_l.go_up,'w')
screen.onkey(paddle_l.go_down,'s')
#=====================================================================================================
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 340 or ball.distance(paddle_l) < 40 and ball.xcor() < -340:
        time.sleep(0.1 * 0.01)
        ball.bounce_x()

    if ball.xcor() > 380:
        score.score_increase_l()
        ball.reset_position()
    if ball.xcor() < -380:
        score.score_increase_r()
        ball.reset_position()
    if score.score_l == 10 or score.score_r == 10 :
        game_is_on = False
        score.game_over()

screen.exitonclick()