import math
import time as t

from constantes import *
from functions import Distance, Verif_Angle
from Sons import gun_sound

sprites = {
    "1": {
        "texture": pg.image.load("Assets/Sprites/Ennemis/test.png"),
        "height": 51,
        "width": 37,
        "ratio": 37 / 51,
        "position": (120, 120),
        "class": "ennemy",
        "HP": 100
    },
    "2": {
        "texture": pg.image.load("Assets/Sprites/Ennemis/test.png"),
        "height": 51,
        "width": 37,
        "ratio": 37 / 51,
        "position": (210, 210),
        "class": "ennemy",
        "HP": 100
    },

    "3": {
        "texture": pg.image.load("Assets/Sprites/greenlight.png"),
        "height": 64,
        "width": 64,
        "ratio": 1,
        "position": (37, 37),
        "class": "neutral"
    },
    
    "4": {
        "texture": pg.image.load("Assets/Sprites/greenlight.png"),
        "height": 64,
        "width": 64,
        "ratio": 1,
        "position": (0,0),
        "class": "NPC"
    
    }
}
coef_angle_tailleX = tailleX / fov_r
max_height = tailleY * 1.5

def Sprite_calcul(player_x, player_y, player_rotation, HEIGHT, dist_list, volume, last_shot, fov_moins, fov_plus, sp_pl_angle, sprite_x, sprite_y, weapon):

        viewed_sprite = False

        if fov_moins <= sp_pl_angle <= fov_plus:

            if sprite["class"] == "ennemy":

                if sprite["HP"]!=0:
                    column = int(abs(coef_angle_tailleX * (sp_pl_angle - HALF_FOV)))
                    # print(column)

                    sprite_distance = Distance(sprite_x - player_x, sprite_y - player_y) * m.cos(sp_pl_angle)

                    if 15 < sprite_distance <= dist_list[int(column // LINE_SIZE)]:
                        print(sp_pl_angle)
                        sprite_height = int(((TS / 1.05) / sprite_distance) * SCREEN_DISTANCE)
                        sprite_width = sprite_height * sprite["ratio"]
                        scaled_sprite = pg.transform.scale(sprite["texture"], (sprite_width, sprite_height))
                        screen.blit(scaled_sprite, (column - sprite_width // 2, (tailleY / 2) - (sprite_height // 2) + HEIGHT))
                        viewed_sprite = True


            else:
                column = int(abs(coef_angle_tailleX * (sp_pl_angle - HALF_FOV)))
                # print(column)

                sprite_distance = Distance(sprite_x - player_x, sprite_y - player_y) * m.cos(sp_pl_angle)

                if 15 < sprite_distance <= dist_list[int(column // LINE_SIZE)]:
                    sprite_height = int(((TS / 1.05) / sprite_distance) * SCREEN_DISTANCE)
                    sprite_width = sprite_height * sprite["ratio"]
                    scaled_sprite = pg.transform.scale(sprite["texture"], (sprite_width, sprite_height))
                    screen.blit(scaled_sprite,
                                (column - sprite_width // 2, (tailleY / 2) - (sprite_height // 2) + HEIGHT))
                    viewed_sprite = True

        left, middle, right = pg.mouse.get_pressed()
        speed, damage = weapons[weapon]["speed"], weapons[weapon]["damage"]

        if left and t.time() - last_shot >= speed:

            gun_sound(weapons[weapon]["sound"], weapons[weapon]["volume"])

            if viewed_sprite:
                attack(sp_pl_angle,damage)
                last_shot = t.time()
                print(last_shot)

        return last_shot



def Sprite_angle(player_x, player_y, sprite_x, sprite_y):
    base_angle = m.atan(abs(sprite_x - player_x) / abs(sprite_y - player_y))

    if player_x > sprite_x and player_y > sprite_y:
        return base_angle

    elif player_x > sprite_x and player_y < sprite_y:
        return m.radians(180) - base_angle

    elif player_x < sprite_x and player_y > sprite_y:
        return m.radians(360) - base_angle

    elif player_x < sprite_x and player_y < sprite_y:
        return m.radians(180) + base_angle


def Sprite(player_x, player_y, player_rotation, HEIGHT, dist_list, volume, last_shot, weapon):
    global sprite
    # Fonction pour afficher les sprites
    for sprite in sprites.values():
        sprite_x, sprite_y = sprite["position"]
        sprite_angle = Sprite_angle(player_x, player_y, sprite_x, sprite_y)
        sp_pl_angle = sprite_angle - player_rotation
        fov_plus, fov_moins = HALF_FOV, - HALF_FOV

        if sprite["class"] == "ennemy":
            if sprite["HP"] > 0:
                last_shot = Sprite_calcul(player_x, player_y, player_rotation, HEIGHT, dist_list, volume, last_shot, fov_moins, fov_plus, sp_pl_angle, sprite_x, sprite_y, weapon)
                
        else: 
            last_shot = Sprite_calcul(player_x, player_y, player_rotation, HEIGHT, dist_list, volume, last_shot, fov_moins, fov_plus, sp_pl_angle, sprite_x, sprite_y, weapon)


    return last_shot



def draw_object():
    for sprite in sprites.values():
        pg.draw.circle(screen, (0, 120, 200), sprite["position"], 4)

    #  Joueur
    pg.draw.circle(screen, (255, 0, 0), (player_x, player_y), 4)
    pg.draw.line(screen, (255, 0, 0), (player_x, player_y),
                 (player_x - 25 * m.sin(player_rotation), player_y - 25 * m.cos(player_rotation)))


def attack(sprite_angle, damage):
    global sprite

    if -0.05 <= sprite_angle <= 0.05 and sprite["class"] == "ennemy":
        sprite["HP"] -= damage
        print("hit")
