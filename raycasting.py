import math as m
import pygame as pg

from constantes import *
from functions import *


def RayCalcul(RayAngle, player_x, player_y, player_rotation):

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

    x_depth = m.floor(player_x / TS) * TS if rx == -1 else m.ceil(player_x / TS) * TS
    y_depth = m.floor(player_y / TS) * TS if ry == -1 else m.ceil(player_y / TS) * TS

    if RayAngle == 0 or m.degrees(RayAngle) == 180 or m.degrees(RayAngle) == 360:
        while not wall:
            y_coord = (player_x, y_depth)
            if not Verif(y_coord[0], y_coord[1], map_number):
                return abs(player_y - y_depth - TS) if (RayAngle == 0 or m.degrees(RayAngle) == 360) else abs(
                    player_y - y_depth), y_coord, "ver"
            y_depth = UpDepth(ry, y_depth)

    elif RayAngle == m.radians(90) or RayAngle == m.radians(270):
        while not wall:
            x_coord = (x_depth, player_y)
            if not Verif(x_coord[0], x_coord[1], map_number):
                return abs(player_x - x_depth - TS) if m.degrees(RayAngle) == 90 else abs(
                    player_x - x_depth), x_coord, "hor"
            x_depth = UpDepth(rx, x_depth)

    else:
        d_y, d_x, check_x, check_y, verif_x, verif_y = 0, 0, 0, 0, False, False

        while not verif_x and check_x < max_check:
            r_coord = player_x - x_depth
            x_coord = (x_depth, player_y + (x_depth - player_x) * x_slope)
            d_x = Distance(r_coord, r_coord * x_slope)
            verif_x = Check(InMap(x_coord[1]), x_coord)
            if not verif_x:
                x_depth = UpDepth(rx, x_depth)
                check_x += 1

        while not verif_y and check_y < max_check:
            r_coord = player_y - y_depth
            y_coord = (player_x + (y_depth - player_y) * y_slope, y_depth)
            d_y = Distance(r_coord, r_coord * y_slope)
            verif_y = Check(InMap(y_coord[1]), y_coord)
            if not verif_y:
                y_depth = UpDepth(ry, y_depth)
                check_y += 1

        # x_coord = (x_depth, player_y + (x_depth - player_x) * x_slope)
        # y_coord = (player_x + (y_depth - player_y) * y_slope, y_depth)
        if verif_x and not verif_y:
            return d_x, x_coord, "ver"

        elif verif_y and not verif_x:
            return d_y, y_coord, "hor"

        elif verif_x and verif_y:
            if d_x <= d_y:
                return d_x, x_coord, "ver"
            else:
                return d_y, y_coord, "hor"
        else:
            return MAX_DEPTH + 1, False, False


def RayCasting(player_x, player_y, player_rotation):

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
        distance, wall_coord, wall_side = RayCalcul(Angle, player_x, player_y, player_rotation)
        if distance < MAX_DEPTH:
            RayDrawing(distance, index, Angle, wall_coord, wall_side, player_x, player_y, player_rotation)



def RayDrawing(distance, line_index, RayAngle, wall_coord, wall_side, player_x, player_y, player_rotation):
    global HEIGHT
    global line_repeat

    # Correction de l'effet de distortion
    distance *= m.cos(RayAngle - player_rotation)
    # color = 255 - ((distance / MAX_DEPTH) * 255)

    if distance < MAX_DEPTH:
        if distance > 1:
            wall_height = int((TS / 1 / distance) * SCREEN_DISTANCE)
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
                    (line_index * LINE_SIZE, slice_y + HEIGHT))  # Affichage prennant en compte le mouv de la souris
