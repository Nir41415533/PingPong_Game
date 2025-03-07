from turtle import Turtle,Screen
from game_look import Game_Screen
from paddle  import Paddle
from ball import Ball
from score_play import Score_Board
import time
score_l=0
score_r=0
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
timer=0.1
game_board=Game_Screen()
paddle_r=Paddle((260,0))
paddle_l=Paddle((-260,0))
ball=Ball()
score_board=Score_Board()

screen.listen()
screen.onkey(paddle_l.go_up,"w")
screen.onkey(paddle_l.go_down,"s")
screen.onkey(paddle_r.go_up,"Up")
screen.onkey(paddle_r.go_down,"Down")


game_is_on=True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 230:
        ball.bounce_x()

    if ball.distance(paddle_l) < 50 and ball.xcor() < -230:
        ball.bounce_x()

    if ball.xcor()>300:
        ball.reset_ball()
        score_board.increase_l_score()

    if ball.xcor()<-300:
        ball.reset_ball()
        score_board.increase_r_score()

    if score_board.l_score==2 or score_board.r_score==2 :
        game_is_on=False
        score_board.clear()
        if score_board.l_score==2 :
            score_board.goto(0,0)
            score_board.write(f"Left Wins", align="center", font=("Arial", 60, "normal"))

        if score_board.r_score== 2:
            score_board.goto(0,0)
            score_board.write(f"Right Wins", align="center", font=("Arial", 60, "normal"))















screen.exitonclick()
