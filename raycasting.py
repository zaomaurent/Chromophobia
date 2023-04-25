import math as m
import pygame as pg

from constantes import *
from functions import *


def RayCalcul(RayAngle, player_x, player_y):
    wall = False
    rot_d = m.degrees(RayAngle)
    sin, cos = m.sin(RayAngle), m.cos(RayAngle)

    x_slope = cos / sin if sin != 0 else False
    y_slope = sin / cos if cos != 0 else False

    if rot_d <= 90 or rot_d == 360:
        rx, ry = -1, -1
    elif 90 < rot_d <= 180:
        rx, ry = -1, 1
    elif 180 < rot_d <= 270:
        rx, ry = 1, 1
    elif rot_d > 270 and rot_d != 360:
        rx, ry = 1, -1

    ############################################################
    x_start = (m.floor(player_x / TS) * TS) + (TS if rx == -1 else 0)

    x_hit_point = (
        x_start,
        player_y + (x_start - player_x) * x_slope
    )

    x_hit = False
    x_distance = 0
    counter = 0

    x_adding = TS * rx
    y_adding = TS * x_slope * ry

    while not x_hit and counter <= max_check:
        x_hit = Check(True, x_hit_point)
        if x_hit:
            x_distance = Distance(x_hit_point[0] - player_x, x_hit_point[1] - player_y)
        else:
            x_hit_point = (x_hit_point[0] + x_adding, x_hit_point[1] + y_adding)
            counter += 1

    ############################################################
    y_start = (m.floor(player_y / TS) * TS) + (TS if ry == -1 else 0)

    y_hit_point = (
        player_x + (y_start - player_y) * y_slope,
        y_start
    )

    y_hit = False
    y_distance = 0
    counter = 0

    x_adding = TS * y_slope * rx
    y_adding = TS * ry

    while not y_hit and counter <= max_check:
        y_hit = Check(True, y_hit_point)
        if y_hit:
            y_distance = Distance(y_hit_point[0] - player_x, y_hit_point[1] - player_y)
        else:
            y_hit_point = (y_hit_point[0] + x_adding, y_hit_point[1] + y_adding)
            counter += 1

    # //////////////////////////////////////////////////////
    if x_hit and not y_hit:
        return x_distance, x_hit_point, "ver"

    elif not x_hit and y_hit:
        return y_distance, y_hit_point, "hor"

    elif x_hit and y_hit:
        if x_distance <= y_distance:
            return x_distance, x_hit_point, "ver"
        else:
            return y_distance, y_hit_point, "hor"
    else:
        return MAX_DEPTH + 1, None, None


def RayCasting(player_x, player_y, player_rotation, HEIGHT, wall_color):
    dist_list = []
    for index in range(int(nb_LINE)):
        Angle = player_rotation - index * RAY_SENSI + HALF_FOV
        Angle_d = m.degrees(Angle)
        if Angle_d >= 360:
            Angle -= m.radians(360)
        if Angle_d < 0:
            Angle += m.radians(360)

        # distance : distance au mur le plus proche aligné au rayon
        # wall_part : le rayon arrive sur une partie du mur, exemple: le milieu ou les bord du mur
        # wall_side : pour savoir si le mur touché est un mur de horizontal ou verticale
        distance, wall_coord, wall_side = RayCalcul(Angle, player_x, player_y)
        dist_list.append(distance)
        if distance < MAX_DEPTH:
            RayDrawing(distance, index, Angle, wall_coord, wall_side, player_rotation, HEIGHT, map["map"], wall_color)

    return dist_list


def RayDrawing(distance, line_index, RayAngle, wall_coord, wall_side, player_rotation, HEIGHT, active_map, wall_color):
    global line_repeat

    # Correction de l'effet de distortion
    distance *= m.cos(RayAngle - player_rotation)

    if distance < MAX_DEPTH:
        if distance > 1:
            wall_height = int(((TS / 1) / distance) * SCREEN_DISTANCE)
        else:
            wall_height = tailleY
        rota_deg = m.degrees(RayAngle)  # Allège le programme en calculs

        # Calcul de la colonne qu'il faut texturer
        wall_part = (wall_coord[0] % TS) / TS if wall_side == "hor" else (wall_coord[1] % TS) / TS

        # -1 pour pouvoir utiliser wall_textures[0]

        if wall_side == "hor":
            if 90 < rota_deg < 270:
                texture_number = active_map[int(wall_coord[1] / TS + 0.01)][int(wall_coord[0] / TS)] - 1
            else:
                texture_number = active_map[int(wall_coord[1] / TS - 0.01)][int(wall_coord[0] / TS)] - 1

        elif wall_side == "ver":
            print(wall_coord)
            if 180 <= rota_deg <= 360 or rota_deg == 0:
                texture_number = active_map[int(wall_coord[1] / TS)][int(wall_coord[0] / TS + 0.01)] - 1
            else:
                texture_number = active_map[int(wall_coord[1] / TS)][int(wall_coord[0] / TS - 0.01)] - 1

        (texture, wall_size) = wall_textures[wall_color][texture_number]
        SLICE_SIZE = m.ceil((wall_size * LINE_SIZE) / 15000)

        # Correction du sens des textures murs. Calculs fait via une texture de fleche pointant vers la droite
        if (wall_side == "ver" and 0 <= rota_deg <= 180) or (wall_side == "hor" and 90 <= rota_deg <= 270):
            wall_part = 1 - wall_part

        # On calcul quelle partie du mur le rayon a atteint
        slice = abs(wall_part * wall_size)

        # creation d'une colonne texturée correspondant a la partie du mur touchée
        column = texture.subsurface(slice if slice + SLICE_SIZE <= wall_size else wall_size - SLICE_SIZE, 0, SLICE_SIZE,
                                    wall_size)

        # Aggrandisement de cette colonne

        column = pg.transform.scale(column, (LINE_SIZE, wall_height))

        # Positionnement de la colonne sur la fenetre
        slice_y = (tailleY / 2) - (wall_height // 2)
        screen.blit(column,
                    (line_index * LINE_SIZE,
                     slice_y + HEIGHT))  # Affichage prennant en compte le mouv de la souris# création du fog

        # Assombrissement des murs en fonction de la distance
        '''color = ((distance / MAX_DEPTH) * 255)
        filtre = pg.Surface(column.get_size())
        filtre.fill((0, 0, 0))
        filtre.set_alpha(color)
        screen.blit(filtre, (line_index * LINE_SIZE, slice_y + HEIGHT))'''
