from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.highest_level = 1
        self.hideturtle()
        self.penup()
        self.goto(-290,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}\nhighest Level: {self.highest_level}", align="left", font=FONT)

    def level_up(self):
        self.level+=1
        self.update_scoreboard()

    def reset(self):
        if self.level>self.highest_level:
            self.highest_level = self.level
        self.level = 1
        self.update_scoreboard()