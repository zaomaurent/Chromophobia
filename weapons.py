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

def gun_sound(sound, volume):
    sound.set_volume(volume)
    sound.play()

def volume_set(sound,volume):
    sound.set_volume(volume)
