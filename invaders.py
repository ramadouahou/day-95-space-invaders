from turtle import Turtle

aliens_xcor = [-200, -150, -100, -50, 0, 50, 100, 150, 200]


class Invaders(Turtle):

    def __init__(self):
        super().__init__()
        self.aliens = []
        self.generate_aliens()
        self.direction = -1

    def generate_aliens(self):
        for x in aliens_xcor:
            alien = Turtle("turtle")
            alien.penup()
            alien.shapesize(stretch_wid=1.5)
            alien.color("green")
            alien.goto(x - 20, 240)
            self.aliens.append(alien)

        for x in aliens_xcor:
            alien = Turtle("turtle")
            alien.penup()
            alien.shapesize(stretch_wid=1.5)
            alien.color("green")
            alien.goto(x, 210)
            self.aliens.append(alien)

        for x in aliens_xcor:
            alien = Turtle("turtle")
            alien.penup()
            alien.shapesize(stretch_wid=1.5)
            alien.color("green")
            alien.goto(x - 20, 180)
            self.aliens.append(alien)

        for x in aliens_xcor:
            alien = Turtle("turtle")
            alien.penup()
            alien.shapesize(stretch_wid=1.5)
            alien.color("green")
            alien.goto(x, 150)
            self.aliens.append(alien)

    def move_aliens(self):
        for alien in self.aliens:
            alien.goto(alien.xcor() + self.direction * 1, alien.ycor())
        self.check_direction()

    def check_direction(self):
        rightmost_alien_x = max(alien.xcor() for alien in self.aliens)
        leftmost_alien_x = min(alien.xcor() for alien in self.aliens)
        if rightmost_alien_x >= 400 or leftmost_alien_x <= -400:
            self.direction *= -1
