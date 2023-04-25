from constantes import *
from functions import Verif, Verif_Angle


def MouseMotion(HEIGHT, player_rotation):
    x, y = mouse.get_pos()
    motion_x, motion_y = MID_POINT[0] - x, MID_POINT[1] - y
    motion_angle = mouse_coef * motion_x

    player_rotation = player_rotation + motion_angle
    player_rotation = Verif_Angle(player_rotation, "rad")

    if motion_y < 0 and HEIGHT > -400:
        HEIGHT += motion_y
    elif motion_y > 0 and HEIGHT < 400:
        HEIGHT += motion_y

    mouse.set_pos(MID_POINT)
    return HEIGHT, player_rotation


def Collision(): # verification des coordonés du joueur (si il est en train d'aller dans un mur)
    hitbox = {
        "top_left": (player_x - current_speed, player_y - current_speed),
        "top_right": (player_x + current_speed, player_y - current_speed),
        "bottom_left": (player_x - current_speed, player_y + current_speed),
        "bottom_right": (player_x + current_speed, player_y + current_speed)
    }
    touche = False
    for hit_point in hitbox.values():
        if not touche:
            touche = not Verif(hit_point[0], hit_point[1], map_number)
    return True if touche else False


def Deplacements(current_speed, speed, HEIGHT, player_x, player_y, player_rotation):
    # player_hitbox = (player_x - 10, player_y - 10, player_x + 10, player_y + 10)
    cos, sin = m.cos(player_rotation), m.sin(player_rotation)
    get_pressed = pg.key.get_pressed()

    if get_pressed[pg.K_LSHIFT]:  # Si le joueur cours
        current_speed = speed * 2

    # Gestion des collision:
    # Les variable équivalent aux positions suivantes si le joueur fait une action (H G B D)

    plus_x, plus_y = current_speed * sin, current_speed * cos  # Bas
    d_x, d_y = current_speed * m.sin(player_rotation + angle), current_speed * m.cos(player_rotation + angle)  # Droite
    g_x, g_y = current_speed * m.sin(player_rotation - angle), current_speed * m.cos(player_rotation - angle)  # Gauche

    # if not Collision():
    if get_pressed[pg.K_z] and Verif(player_x - plus_x, player_y - plus_y, map_number):  # Si la case n'est pas un mur
        player_x, player_y = player_x - plus_x, player_y - plus_y

    if get_pressed[pg.K_s] and Verif(player_x + plus_x, player_y + plus_y, map_number):
        player_x, player_y = player_x + plus_x, player_y + plus_y

    if get_pressed[pg.K_d] and Verif(player_x + d_x, player_y + d_y, map_number):
        player_x, player_y = player_x + d_x, player_y + d_y

    if get_pressed[pg.K_q] and Verif(player_x + g_x, player_y + g_y, map_number):
        player_x, player_y = player_x + g_x, player_y + g_y

    HEIGHT, player_rotation = MouseMotion(HEIGHT, player_rotation)

    return player_x, player_y, player_rotation, HEIGHT
