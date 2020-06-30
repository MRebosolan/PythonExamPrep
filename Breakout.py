import pygame as pg

# initialize
pg.init()
white = (255, 255, 255)

# create window
scr = pg.display.set_mode((800, 800))

# load ball
ballpic = pg.image.load("ball.gif")
ballrect = ballpic.get_rect()

# simulation loop

t = pg.time.get_ticks() * 0.001
x = 50
y = 200
vx = 400
vy = 300

running = True
while t < 10 and running:

    pg.event.pump()

    t0 = t
    t = pg.time.get_ticks() * 0.001
    dt = t - t0

    x = x + vx*dt
    y = y + vy*dt

    if x > 800:
        vx = -vx
        x = 800 - (x - 800)
    elif x < 0:
        vx = -vx
        x = -x

    if y > 800:
        vy = -vy
        y = 800 - (y - 800)
    elif y < 0:
        vy = -vy
        y = -y

    scr.fill(white)

    ballrect.center = (x, y)
    scr.blit(ballpic, ballrect)

    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False



# close window
pg.quit()
