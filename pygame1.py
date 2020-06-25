import pygame as pg

pg.init()

screen = pg.display.set_mode((600,500))
scrrect = screen.get_rect()
pg.draw.circle(screen, (255,255,0), (scrrect.centerx, scrrect.centery), 50, 20)


