import math as m

import pygame as pg
import sys

from constantes import *
from maps import maps


def ExitWindow(
        event):  # fonction qui fait quitter le jeu si le joueur appuye sur quit (boutton defini par ses dimensions)
    if event.type == pg.QUIT:
        pg.quit()
    else:
        return True


def Check(in_map, coord):
    if in_map:
        for x in range(-1, 2):
            for y in range(-1, 2):
                try:
                    if not Verif(coord[0] + x / 80, coord[1] + y / 80, map_number):
                        return True
                except:
                    return True
    return False


def Verif(x_index, y_index, map_number):
    return False if maps[map_number]["map"][int(y_index / TS)][int(x_index / TS)] != 0 else True


def UpDepth(i, depth):
    return depth + TS if i == 1 else depth - TS


def InMap(coord):
    return True if 0 < coord < WDW_SIZE else False


def Distance(a, b):
    return m.sqrt((a ** 2 + b ** 2))  # theoreme de pythagore (calcul de l'hypothenus)


def Verif_Angle(angle, mode):  # fonction qui verifie si l'angle est entre 0 et 360 degrès et qui recale sinon
    if mode == "rad":
        angle = m.degrees(angle)
    if angle < 0:
        angle = 360 + angle
    angle %= 360
    if mode == "rad":
        return m.radians(angle)
    return angle
