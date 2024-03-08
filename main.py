from turtle import Screen
from ship import Ship
from scoreboard import ScoreBoard
from invaders import Invaders
from projectile import Projectile
from projectile_invaders import ProjectileInvaders
from barrier import Barrier
import random
import time

screen = Screen()
screen.setup(width=900, height=720)
screen.bgcolor("black")
screen.title("Rama Space Turtles")
screen.tracer(0)

s = Ship()
i = Invaders()
p = Projectile(s)
pi = ProjectileInvaders()
b = Barrier()
score = ScoreBoard()

screen.listen()
screen.onkey(s.move_left, "a")
screen.onkey(s.move_right, "d")
screen.onkey(p.fire, "space")

game_is_on = True
while game_is_on:
    screen.update()
    i.move_aliens()

    # Ship Projectiles
    if p.state == "fire":
        for projectile in p.projectiles:
            projectile.sety(projectile.ycor() + 5)

    for projectile in p.projectiles:
        if projectile.ycor() > 310:
            projectile.hideturtle()
            p.projectiles.remove(projectile)
            p.state = "ready"

    # Invaders Projectiles
    for projectile in pi.projectiles:
        projectile.sety(projectile.ycor() - 2.5)

    for projectile in pi.projectiles:
        if projectile.ycor() < -340:
            projectile.hideturtle()
            pi.projectiles.remove(projectile)

    roll = random.randint(1, 150)
    if roll == 75:
        alien_to_fire = random.choice(i.aliens)
        pi.fire(alien_to_fire)

    # Projectiles Interaction
    for alien in i.aliens:
        for projectile in p.projectiles:
            if projectile.distance(alien) < 20:
                alien.goto(2000, 2000)
                i.aliens.remove(alien)
                projectile.goto(2000, 2000)
                p.projectiles.remove(projectile)
                p.state = "ready"
                score.point()

    for projectile in pi.projectiles:
        if projectile.distance(s) < 25:
            time.sleep(1)
            s.goto(0, -330)
            projectile.goto(2000, 2000)
            pi.projectiles.remove(projectile)
            score.lose_life()

    for s_projectile in p.projectiles:
        for i_projectile in pi.projectiles:
            if s_projectile.distance(i_projectile) < 20:
                s_projectile.goto(2000, 2000)
                p.projectiles.remove(s_projectile)
                i_projectile.goto(2000, 2000)
                pi.projectiles.remove(i_projectile)
                p.state = "ready"

    # Barrier Interaction
    for barrier in b.barriers:
        for projectile in p.projectiles:
            if projectile.distance(barrier) < 20:
                barrier.goto(2000, 2000)
                b.barriers.remove(barrier)
                projectile.goto(2000, 2000)
                p.projectiles.remove(projectile)
                p.state = "ready"

    for barrier in b.barriers:
        for projectile in pi.projectiles:
            if projectile.distance(barrier) < 20:
                barrier.goto(2000, 2000)
                b.barriers.remove(barrier)
                projectile.goto(2000, 2000)
                pi.projectiles.remove(projectile)

    # etc
    if len(i.aliens) == 0:
        i.generate_aliens()

    if s.xcor() < -420:
        s.setx(-420)

    if s.xcor() > 410:
        s.setx(410)

    if score.life == 0:
        game_is_on = False
        score.game_over()

screen.exitonclick()
