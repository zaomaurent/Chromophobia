import math as m
import pygame as pg
import sys

# Import des autres fonctions du programme
from constantes import *
from interface import *
from menu import *
from mouvement import *
from raycasting import *
from sprites import *


def draw_object():
    for sprite in sprites.values():
        pg.draw.circle(screen, (0, 120, 200), sprite["position"], 4)

    #  Joueur
    pg.draw.circle(screen, (255, 0, 0), (player_x, player_y), 4)
    pg.draw.line(screen, (255, 0, 0), (player_x, player_y),
                 (player_x - 25 * m.sin(player_rotation), player_y - 25 * m.cos(player_rotation)))


def draw_minimap():
    for y, line in enumerate(map["map"]):
        for x, column in enumerate(line):
            pg.draw.rect(
                screen,
                (200, 200, 200) if map["map"][y][x] == 0 else (100, 100, 100),
                (x * TS, y * TS, TS, TS)
            )


Menu()

# Game Loop
while running:

    mouse.set_visible(False)
    pg.display.set_caption(f"Raycasting - {int(clock.get_fps())}")

    for event in pg.event.get():
        ExitWindow(event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:  # Si le joueur veut faire pause
                Pause()
                mouse.set_visible(False)

    # screen.fill((0, 0, 0))

    if mouse.get_focused():
        from constantes import speed

        # speed = speed * (60/clock.get_fps())
        player_x, player_y, player_rotation, HEIGHT = Deplacements(current_speed, speed, HEIGHT, player_x, player_y,
                                                                   player_rotation)
        mid = (tailleY / 2) + HEIGHT
        pg.draw.rect(screen, (50, 50, 50), (0, 0, tailleX, mid))
        pg.draw.rect(screen, (30, 30, 30), (0, mid, tailleX, tailleY - mid))
        dist_list = RayCasting(player_x, player_y, player_rotation, HEIGHT)
        Sprite(player_x, player_y, player_rotation, HEIGHT, dist_list)
        draw_minimap()
        draw_object()
        screen.blit(Crosshair, Crosshair_coord)
    pg.display.flip()
    clock.tick(60)

pg.quit()