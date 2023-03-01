import pygame as pg

from constantes import *

def init():
    global music, gun
    music = pg.mixer.Sound("Assets/Sons/music.mp3")
    volume = 0.5
    gun = pg.mixer.Sound("Assets/Sons/blaster.ogg")
    gun.set_volume(0.7)
    return volume


def f_music(volume):
    global music
    music.set_volume(0)  # volume
    music.play(-1)





def sound_effects(volume):
    global gun

    key_pressed = pg.key.get_pressed()

    if key_pressed[pg.K_UP]:
        volume += 0.01

    if key_pressed[pg.K_DOWN]:
        volume -= 0.01

    #music.set_volume(volume)

def gun_sound(weapon, volume):
    global weapons
    weapons[weapon]["sound"].set_volume(volume)
    weapons[weapon]["sound"].play()
