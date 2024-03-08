from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.life = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(300, 300)
        self.write(f'Score: {self.score}', align="center", font=("Courier", 35, "normal"))
        self.goto(-320, 300)
        self.write(f'Lives: {self.life}', align="center", font=("Courier", 35, "normal"))

    def point(self):
        self.score += 15
        self.update_scoreboard()

    def lose_life(self):
        self.life -= 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 45, "bold"))
