from turtle import Turtle


class ProjectileInvaders(Turtle):

    def __init__(self):
        super().__init__()
        self.projectiles = []

    def fire(self, alien):
        projectile = Turtle("arrow")
        projectile.penup()
        projectile.color("green")
        projectile.right(90)
        projectile.shapesize(stretch_wid=1, stretch_len=1)
        projectile.speed(0.5)
        projectile.goto(alien.xcor(), alien.ycor())
        self.projectiles.append(projectile)
