import time as t
import pygame as pg
# Import des autres fonctions du programme
from constantes import *
from menu import *
from mouvement import *
from raycasting import *
from sprites import *
import Sons as son
from weapons import*

def draw_minimap(): # fonction qui positionne la minimap ou se deplace le joueur en haut a gauche
    for y, line in enumerate(map["map"]):
        for x, column in enumerate(line):
            pg.draw.rect(
                screen,
                (200, 200, 200) if map["map"][y][x] == 0 else (100, 100, 100),
                (x * TS, y * TS, TS, TS)
            )

volume = son.init()
Menu()                  # fonctions principales séparée du game loop
son.f_music(volume)

# Game Loop
while running:

    mouse.set_visible(False)
    pg.display.set_caption(f"Raycasting - {int(clock.get_fps())}")

    for event in pg.event.get():
        ExitWindow(event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:  # Si le joueur veut faire pause 
                son.sound_effects(0)
                Pause() # affiche le menu pause 
                son.sound_effects(volume)
                mouse.set_visible(False)

    # screen.fill((0, 0, 0))

    if mouse.get_focused():
        from constantes import speed

        # speed = speed * (60/clock.get_fps())
        player_x, player_y, player_rotation, HEIGHT = Deplacements(current_speed, speed, HEIGHT, player_x, player_y,
                                                                   player_rotation)
        mid = (tailleY / 2) + HEIGHT
        start = t.time()
        pg.draw.rect(screen, (50, 50, 50), (0, 0, tailleX, mid))
        pg.draw.rect(screen, (30, 30, 30), (0, mid, tailleX, tailleY - mid))
        dist_list = RayCasting(player_x, player_y, player_rotation, HEIGHT)
        son.sound_effects(volume)
        change_weapon(weapon) # echanger entre 2 armes avec les touches du clavier
        Sprite(player_x, player_y, player_rotation, HEIGHT, dist_list, volume, last_shot) # fonction d'affichage des sprites
        draw_minimap()
        draw_object()
        end = t.time()
        screen.blit(Crosshair, Crosshair_coord) # affichage de l'arme
    pg.display.flip()
    clock.tick(60)

pg.mixer.quit()
pg.quit() # ferme la boucle de jeu et donc la fenetre
