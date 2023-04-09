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
        rx, ry, d = -1, -1, True
    elif 90 < rot_d <= 180:
        rx, ry, d = -1, 1, True
    elif 180 < rot_d <= 270:
        rx, ry, d = 1, 1, False
    elif rot_d > 270 and rot_d != 360:
        rx, ry, d = 1, -1, False

    # Raycasting des murs sur l'axe des X <=> |
    ray_point_x = (
        m.floor(player_x / TS) * TS if rx == -1 else m.ceil(player_x / TS) * TS,
        player_y)
    y_adding = 1 / (
        m.tan(x_slope))  # Valeur que l'on ajoute au Y a chaque itération de la boucle <=> parcours la grille
    counter = 0
    while not wall and counter <= max_check:
        if Check(True, ray_point_x):
            x_distance = Distance(player_x - ray_point_x[0], player_y - ray_point_x[1])
            wall = True
        else:
            ray_point_x = (ray_point_x[0] + 1, ray_point_x[1] + y_adding)
            x_distance = 0

    # Raycasting des murs sur l'axe des Y <=> ---
    wall = False
    ray_point_y = (
        player_x,
        m.floor(player_y / TS) * TS if ry == -1 else m.ceil(player_y / TS) * TS)
    x_adding = 1 / (
        m.tan(y_slope))  # Valeur que l'on ajoute au Y a chaque itération de la boucle <=> parcours la grille
    counter = 0

    while not wall and counter <= max_check:
        if Check(True, ray_point_y):
            y_distance = Distance(player_x - ray_point_y[0], player_y - ray_point_y[1])
            wall = True
        else:
            ray_point_y = (ray_point_y[0] + x_adding, ray_point_y[1] + 1)
            y_distance = 0

    if x_distance >= y_distance:
        return x_distance, ray_point_x, "ver"
    elif x_distance <= y_distance:
        return y_distance, ray_point_y, "hor"




def RayCasting(player_x, player_y, player_rotation, HEIGHT):
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
            RayDrawing(distance, index, Angle, wall_coord, wall_side, player_x, player_y, player_rotation, HEIGHT)

    return dist_list


def RayDrawing(distance, line_index, RayAngle, wall_coord, wall_side, player_x, player_y, player_rotation, HEIGHT):
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
                texture_number = map["map"][int(wall_coord[1] / TS + 0.01)][int(wall_coord[0] / TS)] - 1
            else:
                texture_number = map["map"][int(wall_coord[1] / TS - 0.01)][int(wall_coord[0] / TS)] - 1

        elif wall_side == "ver":
            if 180 <= rota_deg <= 360 or rota_deg == 0:
                texture_number = map["map"][int(wall_coord[1] / TS)][int(wall_coord[0] / TS + 0.01)] - 1
            else:
                texture_number = map["map"][int(wall_coord[1] / TS)][int(wall_coord[0] / TS - 0.01)] - 1

        (texture, wall_size) = wall_textures[texture_number]
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
