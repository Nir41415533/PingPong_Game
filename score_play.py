from turtle import Turtle

class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0  # Initialize the left score
        self.r_score = 0  # Initialize the right score
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-50, 260)
        self.write(self.l_score, align="center", font=("Courier", 24, "normal"))
        self.goto(50, 260)
        self.write(self.r_score, align="center", font=("Courier", 24, "normal"))

    def increase_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_r_score(self):
        self.r_score += 1
        self.update_scoreboard()
