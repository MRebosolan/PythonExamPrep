import pygame as pg

pg.init()
reso = (600, 500)
screen = pg.display.set_mode(reso)
scrrect = screen.get_rect()

black = (0, 0, 0)
white = (255, 255, 255)

rocketship = pg.image.load("rocket.png")
rocketrect = rocketship.get_rect()
rocketrect.centerx = 300

for y in range (500, -100, -1):
    rocketrect.centery = y
    pg.draw.rect(screen, white, scrrect)
    screen.blit(rocketship, rocketrect)
    pg.display.flip()

pg.quit()
