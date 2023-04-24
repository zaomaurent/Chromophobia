import pygame as pg
import time as t
from constantes import *

def change_weapon(weapon, weapons):

  for event in pg.event.get():
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_TAB:
        if weapon + 1 in weapons:
          weapon += 1
        else:
          weapon = 1
  return weapon

reload_sound = pg.mixer.Sound("Assets/Sons/reload.mp3")
reload_sound.set_volume(0.4)
def reload(weapons, weapon, reload_start):
  get_pressed = pg.key.get_pressed()

  if weapons[weapon]["mag"] <= 0 or get_pressed[pg.K_r]:
    reload_start = t.time()
    reloading = True
    reload_sound.play()
    weapons[weapon]["mag"] = weapons[weapon]["max_mag"]


  if t.time() - reload_start >= 2:
    reloading = False
  else:
    reloading = True

  return reloading, reload_start

QUANTUM = pg.font.Font('Assets\Quantum.otf', 100)

def mag_print(weapons, weapon):
  text = str(weapons[weapon]["mag"]) + " ! " + str(weapons[weapon]["max_mag"])
  mag_info = QUANTUM.render(text, True, (255, 255, 255))
  screen.blit(mag_info, (20, tailleY - 120))
