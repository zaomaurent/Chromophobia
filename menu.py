import time
import webbrowser
import sys

from constantes import *
from functions import ExitWindow


def IsClicked(coord, ex, ey, x=0, y=0):
    if coord[0] + x <= ex <= coord[2] + x and coord[1] + y <= ey <= coord[3] + y:
        return True
    else:
        return False


def FonduIn():
    fondu = pg.Surface((tailleX, tailleY))
    fondu.fill((0, 0, 0))
    for alpha in range(255):
        fondu.set_alpha(1)
        screen.blit(fondu, (0, 0))
        pg.display.flip()


def dark_bg(alpha):  # Pour rendre le fond plus sombre

    Surface = pg.Surface((tailleX, tailleY))
    Surface.set_alpha(alpha)
    Surface.fill((15, 15, 15))
    screen.blit(Surface, (0, 0))
    pg.display.flip()



def Menu():
    mouse.set_visible(True)
    debut = time.time()
    Menu_Button = [
        [420, 221, 1179, 374],
        [450, 221, 1146, 552],
        [562, 555, 1038, 652],
        [0, 745, 372, 800]
    ]

    menu = pg.image.load("Assets/GUI/menu.png")
    menu_running = True
    while menu_running:
        clock.tick(60)
        for event in pg.event.get():
            menu_running = ExitWindow(event)

        get_clicked = mouse.get_pressed()
        if get_clicked[0]:
            ex, ey = mouse.get_pos()
            for index, button in enumerate(Menu_Button):
                anti_spam = time.time() - debut > 0.75
                if IsClicked(button, ex, ey, 0, 0):
                    if index == 0 and anti_spam:
                        FonduIn()
                        mouse.set_visible(False)
                        return
                    elif index == 1 and anti_spam:
                        Parametres(background)
                        mouse.set_visible(False)
                        return
                    elif index == 2 and anti_spam:
                        sys.exit()
                        return
                    elif index == 3:
                        webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        screen.blit(background, (0, 0))
        screen.blit(menu, (0, 0))
        pg.display.flip()


def Parametres(background):
    mouse.set_visible(True)
    debut = time.time()
    settings_button = [
        [32, 109, 149, 132],
        [32, 178, 250, 201],
        [32, 247, 274, 272],
        [32, 317, 190, 341],
        [32, 380, 182, 404]
    ]

    settings_running = True
    settings = pg.image.load("Assets/GUI/parametres.png")

    while settings_running:
        get_clicked = False
        for event in pg.event.get():
            settings_running = ExitWindow(event)
            if event.type == pg.MOUSEBUTTONDOWN:
                get_clicked = True
                ex, ey = mouse.get_pos()
        if get_clicked:
            anti_spam = time.time() - debut > 1.5
            for index, button in enumerate(settings_button):
                if IsClicked(button, ex, ey):
                    if index == 0 and anti_spam:
                        print("Audio")
                    elif index == 1 and anti_spam:
                        print("Graphique")
                    elif index == 2 and anti_spam:
                        print("Cmds")
                    elif index == 3 and anti_spam:
                        print("Succes")
                    elif index == 4 and anti_spam:
                        print("Close")

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(settings, (0, 0))
        pg.display.flip()
    return


def Pause():
    mouse.set_visible(True)
    Button_Coord = [
        [15, 17, 788, 144],
        [15, 166, 788, 288],
        [15, 314, 380, 436],
        [422, 314, 787, 436],
        [15, 463, 787, 585],
    ]
    menu_pause = pg.image.load("Assets/GUI/button.png")
    x, y, h, w = (tailleX / 4), (tailleY / 8), (tailleX / 2), ((tailleY / 8) * 6)

    inpause = True

    dark_bg(220)
    while inpause:

        for event in pg.event.get():
            ExitWindow(event)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return
            pg.display.flip()
            clock.tick(60)

        get_clicked = mouse.get_pressed()
        screen.blit(menu_pause, (x, y))
        if get_clicked[0]:
            ex, ey = mouse.get_pos()
            for index, button in enumerate(Button_Coord):
                if IsClicked(button, ex, ey, x, y):
                    if index == 0:
                        inpause = False
                        mouse.set_pos(MID_POINT)
                    elif index == 1:
                        Parametres(background)
                    elif index == 2:
                        print("Maps")
                    elif index == 3:
                        sys.exit()
                    elif index == 4:
                        inpause = False
                        FonduIn()
                        Menu()
