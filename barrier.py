from turtle import Turtle

barrier_cor = [-350, -330, -100, -50, 0, 50, 100, 150, 350]


class Barrier(Turtle):

    def __init__(self):
        super().__init__()
        self.barriers = []
        self.generate_barriers()

    def generate_barriers(self):
        cor1 = -350
        for x in range(7):
            barrier = Turtle("square")
            barrier.penup()
            barrier.color("white")
            barrier.goto(cor1 + 20, -75)
            cor1 += 20
            self.barriers.append(barrier)

        cor2 = -100
        for x in range(7):
            barrier = Turtle("square")
            barrier.penup()
            barrier.color("white")
            barrier.goto(cor2 + 20, -75)
            cor2 += 20
            self.barriers.append(barrier)

        cor3 = 150
        for x in range(7):
            barrier = Turtle("square")
            barrier.penup()
            barrier.color("white")
            barrier.goto(cor3 + 20, -75)
            cor3 += 20
            self.barriers.append(barrier)

        cor4 = -350
        for x in range(7):
            barrier = Turtle("square")
            barrier.penup()
            barrier.color("white")
            barrier.goto(cor4 + 20, -55)
            cor4 += 20
            self.barriers.append(barrier)

        cor5 = -100
        for x in range(7):
            barrier = Turtle("square")
            barrier.penup()
            barrier.color("white")
            barrier.goto(cor5 + 20, -55)
            cor5 += 20
            self.barriers.append(barrier)

        cor6 = 150
        for x in range(7):
            barrier = Turtle("square")
            barrier.penup()
            barrier.color("white")
            barrier.goto(cor6 + 20, -55)
            cor6 += 20
            self.barriers.append(barrier)
