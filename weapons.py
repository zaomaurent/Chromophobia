import pygame as pg

def change_weapon(weapon, weapons):

  for event in pg.event.get():
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_RETURN:
        if weapon + 1 in weapons:
          print("weapon :",  weapons[weapon]["name"])
          weapon += 1
          print("weapon next :",  weapons[weapon]["name"])
        else:
          weapon = 1
          print("weapon reset :", weapons[weapon]["name"])
  return weapon
