import pygame as pg
from pprint import pprint
from functions import *
from constantes import *


def map_creator():
    # size = int(input("Quelle est la taille de la map ? : "))
    size = 40
    map = []
    for a in range(size):
        map.append([])
    for a in range(-1, 1):
        for b in range(size):
            map[a].append(1)
    for a in range(1, size-1):
        map[a].append(1)
        for b in range(size - 2):
            map[a].append(0)
        map[a].append(1)

    TS = 25 # tile_size
    EFFECTIVE_TS = TS + 1
    map_x, map_y = len(map[0]), len(map)
    emap_x, emap_y = map_x * EFFECTIVE_TS, map_y * EFFECTIVE_TS
    print(emap_x, emap_y)
    button_x, button_y = emap_x + 3 * EFFECTIVE_TS, 3 * EFFECTIVE_TS
    MODE = [0, 1]
    CHANGE_MOD = pg.Rect(button_x, button_y, EFFECTIVE_TS * 5, EFFECTIVE_TS)
    SAVING = pg.Rect(button_x, button_y + EFFECTIVE_TS * 2, EFFECTIVE_TS * 5, EFFECTIVE_TS)
    QUANTUM = pg.font.Font('Assets\Quantum.otf', 30)
    running = True

    while running:
        screen.fill((0, 0, 0))

        for y, line in enumerate(map):
            for x, tile in enumerate(line):
                pg.draw.rect(
                    screen,
                    (200, 200, 200) if map[y][x] == 0 else (100, 100, 100),
                    (x * EFFECTIVE_TS, y * EFFECTIVE_TS, TS, TS))

        get_pressed = pg.mouse.get_pressed()

        if MODE[0]:
            text = "Gomme"
        elif MODE[1]:
            text = "Crayon"

        text_button = QUANTUM.render(text, True, (255, 255, 255), (100, 100, 100))
        saving_button = QUANTUM.render("Sauvegarder", True, (255, 255, 255), (100, 100, 100))
        screen.blit(text_button, (button_x, button_y))
        screen.blit(saving_button, (button_x, button_y + EFFECTIVE_TS * 2))

        if get_pressed[0]:
            x, y = pg.mouse.get_pos()
            index = (int(y // EFFECTIVE_TS), int(x // EFFECTIVE_TS))
            print(index, x, y)

            if 0 < x < emap_x and 0 < y < emap_y:
                tile = map[index[0]][index[1]]
                if tile == MODE[0]:
                    print(map[index[0]][index[1]])
                    map[index[0]][index[1]] = MODE[1]

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if CHANGE_MOD.collidepoint(event.pos):
                    if MODE == [1, 0]:
                        MODE = [0, 1]
                    elif MODE == [0, 1]:
                        MODE = [1, 0]
                if SAVING.collidepoint(event.pos):
                    running = False


        pg.display.flip()
        clock.tick(60)

    pprint(map, indent=2)



