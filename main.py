from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()
ball = Ball()
paddle_right = Paddle(350,0)
paddle_left = Paddle(-350,0)

screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

screen.onkey(paddle_left.go_up, "Left")
screen.onkey(paddle_left.go_down, "Right")


game_isnot_over = True
while game_isnot_over:
  screen.update()
  time.sleep(.1)

  ball.move()
  #Detecting collision with wall
  if ball.ycor() >280 or ball.ycor() < -280:
    #need to bounce
    ball.bounce_y()
  #Detect collision with right and left Paddle
  if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
    ball.bounce_x()
  #Detect if ball cross right wall
  if ball.xcor() > 380:
    ball.reset_position()
    scoreboard.l_score += 1
    scoreboard.update_scoreboard()
  #Detect if ball cross left wall
  if ball.xcor() < -380:
    ball.reset_position()
    scoreboard.r_score += 1
    scoreboard.update_scoreboard()

  if scoreboard.r_score  >= 10 or scoreboard.l_score  >= 10:
    game_isnot_over = False
    scoreboard.game_over()
screen.exitonclick()
