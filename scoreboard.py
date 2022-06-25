from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font =("Courier", 80, "normal") )
        self.goto(100,200)
        self.write(self.r_score, align="center", font =("Courier", 80, "normal") )

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("courier",24,"normal"))
        self.goto(0,50)
        if self.r_score >= 10:
             self.write("Right side is the winner", align="center", font=("courier",24,"normal"))
        elif self.l_score >= 10:
             self.write("left side is the winner", align="center", font=("courier",24,"normal"))