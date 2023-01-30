import pygame as pg
import sys

from constantes import *
from maps import maps


def ExitWindow(event):
    if event.type == pg.QUIT:
        sys.exit()
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
    else:
        return False


def Verif(x_index, y_index, map_number):
    return False if maps[map_number]["map"][int(y_index / TS)][int(x_index / TS)] != 0 else True


def UpDepth(i, depth):
    return depth + TS if i == 1 else depth - TS


def InMap(coord):
    return True if 0 < coord < WDW_SIZE else False


def Distance(a, b):
    return m.sqrt((a ** 2 + b ** 2))


def Mouv_cam(height, current_speed):
    global max_height,min_height, cam_mouv

    if max_height<=height:
        cam_mouv = -1

    elif min_height>=height:
        cam_mouv = 1


    height += cam_mouv * current_speed
