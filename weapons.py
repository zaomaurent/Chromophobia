import constantes

def change_weapons(weapon):
  global weapons
  for event in pg.event.get():
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_RETURN:
        if weapon + 1 in weapons:
          weapon += 1
        else:
          weapon = 1
