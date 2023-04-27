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
                (x * TS, y * TS, TS, TS))
    for sprite in map["sprites"].values():
        if sprite["class"] != "ennemy":
            pg.draw.circle(screen, (0, 255, 120), sprite["position"], 3)

volume = son.init()

# On envoie le joueur ds le menu
Menu()  # fonctions principales séparée du game loop
son.f_music(volume)

# Game Loop
color_timer = t.time()
break_timer = color_timer
change_color = True
while running:

    if mouse.get_focused():
        mouse.set_visible(False)
        fps = clock.get_fps()
        pg.display.set_caption(f"Raycasting - {int(fps)}") # Change le titre de la fenetre avec les fps

        get_pressed = pg.key.get_pressed()
        if get_pressed[pg.K_ESCAPE] and t.time() - break_timer > 0.5:
            son.music.set_volume(0)
            change_color = Pause(change_color)  # affiche le menu pause
            mouse.set_visible(False)
            break_timer = t.time()

        son.music.set_volume(0.1)

        for event in pg.event.get():
            ExitWindow(event)

        from constantes import speed

        speed_ratio = 60/fps
        speed = speed_ratio
        speed_multiplier = 2/speed_ratio
        # Permet au joueur de se deplacer et de gerer les collisions
        player_x, player_y, player_rotation, HEIGHT = Deplacements(current_speed, speed, speed_multiplier,
                                                                   HEIGHT, player_x, player_y,
                                                                   player_rotation)
        # calcul du milieu effectif de l'ecran, avc l'angle de vue (haut/bas) du joueur
        mid = MID_POINT[1] + HEIGHT

        # Affichage de 2 rectangles représentant le sol et le plafond de 2 couleurs différentes
        pg.draw.rect(screen, (50, 50, 50), (0, 0, tailleX, mid))
        pg.draw.rect(screen, (30, 30, 30), (0, mid, tailleX, tailleY - mid))

        # Calcul de la position des murs <=> moteur graphique du jeu, il retourne une liste de distance pour
        # l'affichage des sprites
        dist_list = RayCasting(player_x, player_y, player_rotation, HEIGHT, wall_color)

        # Echanger entre 2 armes avec les touches du clavier
        weapon = change_weapon(weapon, weapons)

        # Fonction d'affichage des sprites
        last_shot, player_hp, dead_mobs = Sprite(player_x, player_y, player_rotation, HEIGHT, dist_list, last_shot, weapon, map["sprites"], reloading, dead_mobs)

        # Affichage de la minimap en haut à gauche
        draw_minimap()

        QUANTUM = pg.font.Font('Assets\Quantum.otf', 20)

        #Affichage de la barre de vie
        pg.draw.rect(screen, (0,255,0), (tailleX/2 - 250, tailleY - 50, player_hp, 20))
        hp_text = str(player_hp) + " ! 500"
        HP_info = QUANTUM.render(hp_text, True, (255, 255, 255))
        screen.blit(HP_info, (tailleX/2 - 250, tailleY - 80))

        QUANTUM = pg.font.Font('Assets\Quantum.otf', 50)

        mob_text = str(dead_mobs) + "x "
        mob_info = QUANTUM.render(mob_text, True, (255, 255, 255))
        screen.blit(mob_info, (tailleX - 140, 20))
        mob = pg.image.load("Assets/Sprites/Ennemis/test.png")
        screen.blit(mob, (tailleX - 60, 20))


        # Affichage de la position des ennemis sur la minimap
        draw_object(map["sprites"], player_x, player_y, player_rotation)

        screen.blit(Crosshair, Crosshair_coord)  # Affichage du viseur

        if not reloading:
            screen.blit(weapons[weapon]["texture"], weapons[weapon]["coord"])

        if player_hp <= 0:
            son.music.set_volume(0)
            player_hp, dead_mobs, player_x, player_y, player_rotation = Game_over(map["sprites"])
            running = False

        if dead_mobs == map["mob_quantity"]:
            son.music.set_volume(0)
            player_hp, dead_mobs, player_x, player_y, player_rotation = Victory(map["sprites"])
            Menu()

        reloading, reload_start = reload(weapons, weapon, reload_start, reloading)

        mag_print(weapons, weapon)

        if change_color:
            color_timer_difference = t.time() - color_timer
            if color_timer_difference >= player_hp/80 + 0.8:
                color_timer += color_timer_difference
                if wall_color != 3:
                    wall_color += 1
                else:
                    wall_color = 0

            clock.tick(60)
        pg.display.flip()


pg.mixer.quit()
pg.quit()  # Ferme la boucle de jeu et donc la fenetre
