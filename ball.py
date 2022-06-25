from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.y_move = 20
    self.x_move = 10

  def move(self):
    x_new = self.xcor() + self.x_move
    y_new = self.ycor() + self.y_move
    self.penup()
    self.goto(x_new, y_new)

  def bounce_y(self):
    self.y_move *= -1

  def bounce_x(self):
    self.x_move *= -1

  def reset_position(self):
    self.goto(0, 0)
    self.bounce_x()