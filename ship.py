from turtle import Turtle


class Ship(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("arrow")
        self.color("white")
        self.left(90)
        self.shapesize(stretch_wid=3, stretch_len=3)
        self.speed(0)
        self.goto(0, -330)

    def move_left(self):
        self.goto(self.xcor() - 30, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + 30, self.ycor())
