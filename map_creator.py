import pygame as pg
from pprint import pprint
from functions import *
from constantes import *


def main():
    #size = int(input("Quelle est la taille de la map (map carrée) : "))
    map = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]


main()

TS = 25
EFFECTIVE_TS = TS + 1
map_x, map_y = len(base_map[0]), len(base_map)
emap_x, emap_y = map_x * EFFECTIVE_TS, map_y * EFFECTIVE_TS
button_x, button_y = emap_x + 3 * EFFECTIVE_TS, 3 * EFFECTIVE_TS
MODE = [0, 1]
CHANGE_MOD = pg.Rect(button_x, button_y, EFFECTIVE_TS * 5, EFFECTIVE_TS)
QUANTUM = pg.font.Font('Ressources & autres\Quantum.otf', 30)

while running:
    screen.fill((0, 0, 0))

    for y, line in enumerate(base_map):
        for x, tile in enumerate(line):
            pg.draw.rect(
                screen,
                (200, 200, 200) if base_map[y][x] == 0 else (100, 100, 100),
                (x * EFFECTIVE_TS, y * EFFECTIVE_TS, TS, TS))

    get_pressed = pg.mouse.get_pressed()

    if MODE[0]:
        text = "Gomme"
    elif MODE[1]:
        text = "Crayon"

    text_button = QUANTUM.render(text, True, (255, 255, 255), (100, 100, 100))
    screen.blit(text_button, (button_x, button_y))

    if get_pressed[0]:
        x, y = pg.mouse.get_pos()
        index = (int(y // EFFECTIVE_TS), int(x // EFFECTIVE_TS))

        if 0 < x < emap_x and 0 < y < emap_y:
            tile = base_map[index[0]][index[1]]
            if tile == MODE[0]:
                base_map[index[0]][index[1]] = MODE[1]

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if CHANGE_MOD.collidepoint(event.pos):
                if MODE == [1, 0]:
                    MODE = [0, 1]
                elif MODE == [0, 1]:
                    MODE = [1, 0]

    pg.display.flip()
    clock.tick(60)

pprint(base_map, indent=2)
