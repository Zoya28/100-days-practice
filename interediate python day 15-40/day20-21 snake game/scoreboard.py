from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.current_score = 0
        self.penup()
        self.setpos(0, 230)
        self.write(
            f"Score: {self.current_score}",
            False,
            ALIGNMENT,
            FONT
        )
        self.hideturtle()
    def increase_score(self):
        self.clear()
        self.current_score += 1
        self.write(
            f"Score: {self.current_score}", False, "center", ("Arial", 12, "normal")
        )
    def game_over(self):
        self.setpos(0, 0)
        self.write(
            f"GAME OVER!", False, "center", ("Arial", 15, "normal")
        )
        
