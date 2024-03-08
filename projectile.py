from turtle import Turtle


class Projectile(Turtle):

    def __init__(self, ship):
        super().__init__()
        self.projectiles = []
        self.ship = ship
        self.state = "ready"

    def fire(self):
        if self.state == "ready":
            self.state = "fire"
            projectile = Turtle("classic")
            projectile.penup()
            projectile.color("white")
            projectile.left(90)
            projectile.shapesize(stretch_wid=1, stretch_len=1)
            projectile.speed(0.5)
            projectile.goto(self.ship.xcor(), self.ship.ycor())
            self.projectiles.append(projectile)

