from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(50, 255)
        self.write(arg=self.r_score, align="left", font=("Arial", 25, "normal"))
        self.goto(-50, 255)
        self.write(arg=self.l_score, align="left", font=("Arial", 25, "normal"))

    def l_update(self):
        self.l_score +=1
        self.update()

    def r_update(self):
        self.r_score +=1
        self.update()
