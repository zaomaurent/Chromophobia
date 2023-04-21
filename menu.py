import time
import typing
import webbrowser
import sys

from constantes import *
from functions import ExitWindow
from map_creator import *


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
        (420, 221, 1179, 374),
        (450, 221, 1146, 552),
        (562, 555, 1038, 652),
        (0, 745, 372, 800)
    ]

    menu = pg.image.load("Assets/GUI/menu.png")
    menu_running = True
    while menu_running:
        clock.tick(60)
        for event in pg.event.get():
            menu_running = ExitWindow(event)

        get_clicked = mouse.get_pressed()
        if get_clicked[0]:
            mx, my = mouse.get_pos()
            for index, button in enumerate(Menu_Button):
                anti_spam = time.time() - debut > 0.75
                if IsClicked(button, mx, my):
                    if index == 0 and anti_spam:
                        if not Modes_De_Jeu(background):  # es ce que le joueur est allé en partie ou est revenu au menu
                            FonduIn()
                            mouse.set_visible(False)
                            return  # On va ds la boucle principale du jeu => la partie 3d

                    elif index == 1 and anti_spam:
                        Parametres(background)
                    elif index == 2 and anti_spam:
                        sys.exit()
                    elif index == 3:
                        webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        screen.blit(background, (0, 0))
        screen.blit(menu, (0, 0))
        pg.display.flip()


def Modes_De_Jeu(background):
    buttons = [
        (616, 336, 995, 370),
        (616, 426, 995, 470),
        (0, 0, 136, 67)
    ]
    GUI = pg.image.load("Assets/GUI/games_modes.png")
    clicked = False
    debut = time.time()
    while True:
        clock.tick(60)

        for e in pg.event.get():
            if not ExitWindow(e):  # Si l'utilisateur ferme la fenetre
                sys.exit()
            if e.type == pg.MOUSEBUTTONDOWN:
                clicked = True
            else:
                clicked = False
        if clicked:
            mx, my = mouse.get_pos()
            for index, button in enumerate(buttons):
                anti_spam = time.time() - debut > 0.75
                if anti_spam:
                    if IsClicked(button, mx, my):
                        if index == 0:
                            return False
                        if index == 1:
                            map_creator()
                        if index == 2:
                            return True
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(GUI, (0, 0))
        pg.display.flip()


def Parametres(background):
    mouse.set_visible(True)
    debut = time.time()
    settings_button = [
        (32, 109, 149, 132),
        (32, 178, 250, 201),
        (32, 247, 274, 272),
        (32, 317, 190, 341),
        (32, 385, 211, 410)
    ]
    settings = pg.image.load("Assets/GUI/parametres.png")

    while True:
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
                    if anti_spam:
                        if index == 0:
                            print("Audio")
                        elif index == 1:
                            print("Graphique")
                        elif index == 2:
                            print("Cmds")
                        elif index == 3:
                            print("Succes")
                        elif index == 4:
                            return

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(settings, (0, 0))
        pg.display.flip()
    return


def Pause(change_color):
    mouse.set_visible(True)
    Button_Coord = [
        (15, 17, 788, 144),
        (15, 166, 788, 288),
        (15, 314, 380, 436),
        (422, 314, 787, 436),
        (15, 463, 787, 585),
    ]
    menu_pause = pg.image.load("Assets/GUI/button.png")
    x, y, h, w = (tailleX / 4), (tailleY / 8), (tailleX / 2), ((tailleY / 8) * 6)

    inpause = True

    dark_bg(220)
    anti_spam = t.time()
    while inpause:

        for event in pg.event.get():
            ExitWindow(event)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return change_color

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
                        return change_color
                    elif index == 2 and t.time() - anti_spam >= 1:
                        anti_spam = t.time()
                        if change_color:
                            change_color = False
                            print("Changement de couleur désactivé" + str(change_color))
                        else:
                            change_color = True
                            print("Changement de couleur activé")
                    elif index == 3:
                        sys.exit()
                    elif index == 4:
                        inpause = False
                        FonduIn()
                        Menu()
        pg.display.flip()
        clock.tick(60)
    return change_color
