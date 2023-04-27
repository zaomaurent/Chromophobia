import pygame as pg

from constantes import *


def init():
    global music, gun
    music = pg.mixer.Sound("Assets/Sons/music.mp3")
    volume = 0.5
    return volume


def f_music(volume):
    global music
    music.set_volume(0.1)  # volume
    music.play(-1)


def sound_effects(volume):

    key_pressed = pg.key.get_pressed()

    if key_pressed[pg.K_UP]:
        volume += 0.01

    if key_pressed[pg.K_DOWN]:
        volume -= 0.01

    #music.set_volume(volume)

def gun_sound(sound, volume):
    sound.set_volume(volume)
    sound.play()
