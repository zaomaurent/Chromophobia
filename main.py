import time as t
import pygame as pg

# Import des autres fonctions du programme
from constantes import *
from menu import *
from mouvement import *
from raycasting import *
from sprites import *
import Sons as son
from weapons import *


# from ATH import *

def draw_minimap():  # fonction qui affiche la carte où se déplace le joueur; En haut à gauche de la fenetre
    for y, line in enumerate(map["map"]):
        for x, column in enumerate(line):
            pg.draw.rect(
                screen,
                (200, 200, 200) if map["map"][y][x] == 0 else (100, 100, 100),
                (x * TS, y * TS, TS, TS)
            )
    for sprite in map["sprites"].values():
        pg.draw.circle(screen, (0, 255, 120), sprite["position"], 3)


volume = son.init()

# On envoie le joueur ds le menu
Menu()  # fonctions principales séparée du game loop
son.f_music(volume)

# Game Loop
while running:

    mouse.set_visible(False)
    pg.display.set_caption(f"Raycasting - {int(clock.get_fps())}") # Change le titre de la fenetre avec les fps

    for event in pg.event.get():
        ExitWindow(event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:  # Si le joueur veut faire pause 
                son.sound_effects(0)
                Pause()  # affiche le menu pause
                son.sound_effects(volume)
                mouse.set_visible(False)

    if mouse.get_focused():
        from constantes import speed

        # Permet au joueur de se deplacer et de gerer les collisions
        player_x, player_y, player_rotation, HEIGHT = Deplacements(current_speed, speed,
                                                                   HEIGHT, player_x, player_y,
                                                                   player_rotation)
        # calcul du milieu effectif de l'ecran, avc l'angle de vue (haut/bas) du joueur
        mid = MID_POINT[1] + HEIGHT

        # Affichage de 2 rectangles représentant le sol et le plafond de 2 couleurs différentes
        pg.draw.rect(screen, (50, 50, 50), (0, 0, tailleX, mid))
        pg.draw.rect(screen, (30, 30, 30), (0, mid, tailleX, tailleY - mid))

        # Calcul de la position des murs <=> moteur graphique du jeu, il retourne une liste de distance pour l'affichage des sprites
        dist_list = RayCasting(player_x, player_y, player_rotation, HEIGHT)

        son.sound_effects(volume)  # Appel de la fonction des bruitages

        # Echanger entre 2 armes avec les touches du clavier
        weapon = change_weapon(weapon, weapons)

        # Fonction d'affichage des sprites
        last_shot = Sprite(player_x, player_y, player_rotation, HEIGHT, dist_list, last_shot, weapon, map["sprites"])

        # Affichage de la minimap en haut à gauche
        draw_minimap()

        # Affichage de la position des ennemis sur la minimap
        draw_object(map["sprites"], player_x, player_y, player_rotation)

        # HP_indicator(50)

        screen.blit(Crosshair, Crosshair_coord)  # Affichage du viseur
    pg.display.flip()
    clock.tick(60)

pg.mixer.quit()
pg.quit()  # Ferme la boucle de jeu et donc la fenetre
