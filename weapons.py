import pygame as pg
import time as t
from constantes import *


def change_weapon(weapon, weapons):
    for event in pg.event.get():
        if event.type == pg.MOUSEWHEEL:
            if weapon + 1 in weapons:
                weapon += 1
            else:
                weapon = 1
    return weapon

reload_sound = pg.mixer.Sound("Assets/Sons/reload_sound.ogg")
reload_sound.set_volume(0.4)

def reload(weapons, weapon, reload_start, reloading):
    get_pressed = pg.key.get_pressed()

    if (weapons[weapon]["mag"] <= 0 or get_pressed[pg.K_r]) and not reloading:
        reload_start = t.time()
        reloading = True
        reload_sound.play(0)
        print("reload")
        weapons[weapon]["mag"] = weapons[weapon]["max_mag"]

    if t.time() - reload_start >= 2:
        reloading = False
    else:
        reloading = True

    return reloading, reload_start


QUANTUM = pg.font.Font('Assets\Quantum.otf', 75)
bullet_logo = pg.transform.scale(pg.image.load("Assets/bullet_logo.png"), (30,75))

def mag_print(weapons, weapon):
    text = str(weapons[weapon]["mag"]) + " ! " + str(weapons[weapon]["max_mag"])
    mag_info = QUANTUM.render(text, True, (255, 255, 255))
    screen.blit(mag_info, (60, tailleY - 95))
    screen.blit(bullet_logo, (20, tailleY - 95))