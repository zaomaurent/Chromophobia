from pprint import pprint


def f_verifligne(hauteur, longueur, alignement_de_4_pions, couleur, tab):
    if tab[hauteur][0] == couleur and tab[hauteur][1] == couleur and tab[hauteur][2] == couleur and tab[hauteur][
        3] == couleur:
        alignement_de_4_pions = False
    elif tab[hauteur][1] == couleur and tab[hauteur][2] == couleur and tab[hauteur][3] == couleur and tab[hauteur][
        4] == couleur:
        alignement_de_4_pions = False
    elif tab[hauteur][2] == couleur and tab[hauteur][3] == couleur and tab[hauteur][4] == couleur and tab[hauteur][
        5] == couleur:
        alignement_de_4_pions = False
    elif tab[hauteur][3] == couleur and tab[hauteur][4] == couleur and tab[hauteur][5] == couleur and tab[hauteur][
        6] == couleur:
        alignement_de_4_pions = False
    return alignement_de_4_pions


def f_verifcolonne(hauteur, longueur, alignement_de_4_pions, couleur, tab):
    if tab[0][longueur] == couleur and tab[1][longueur] == couleur and tab[2][longueur] == couleur and tab[3][
        longueur] == couleur:
        alignement_de_4_pions = False
    elif tab[1][longueur] == couleur and tab[2][longueur] == couleur and tab[3][longueur] == couleur and tab[4][
        longueur] == couleur:
        alignement_de_4_pions = False
    elif tab[2][longueur] == couleur and tab[3][longueur] == couleur and tab[4][longueur] == couleur and tab[5][
        longueur] == couleur:
        alignement_de_4_pions = False
    return alignement_de_4_pions


def f_verifdiago(hauteur, longueur, alignement_de_4_pions, couleur, tab):
    if tab[2][0] == couleur and tab[3][1] == couleur and tab[4][2] == couleur and tab[5][3] == couleur:
        alignement_de_4_pions = False
    elif tab[1][0] == couleur and tab[2][1] == couleur and tab[3][2] == couleur and tab[5][3] == couleur:
        alignement_de_4_pions = False
    elif tab[2][1] == couleur and tab[3][2] == couleur and tab[4][3] == couleur and tab[5][4] == couleur:
        alignement_de_4_pions = False
    elif tab[0][0] == couleur and tab[1][1] == couleur and tab[2][2] == couleur and tab[3][3] == couleur:
        alignement_de_4_pions = False
    elif tab[4][4] == couleur and tab[1][1] == couleur and tab[2][2] == couleur and tab[3][3] == couleur:
        alignement_de_4_pions = False
    elif tab[4][4] == couleur and tab[5][5] == couleur and tab[2][2] == couleur and tab[3][3] == couleur:
        alignement_de_4_pions = False
    elif tab[0][2] == couleur and tab[1][3] == couleur and tab[2][4] == couleur and tab[3][5] == couleur:
        alignement_de_4_pions = False
    elif tab[1][2] == couleur and tab[2][3] == couleur and tab[3][4] == couleur and tab[4][5] == couleur:
        alignement_de_4_pions = False
    elif tab[0][3] == couleur and tab[1][4] == couleur and tab[2][5] == couleur and tab[3][6] == couleur:
        alignement_de_4_pions = False
    return alignement_de_4_pions


def f_verifautrediago(hauteur, longueur, alignement_de_4_pions, couleur, tab):
    if tab[0][3] == couleur and tab[1][2] == couleur and tab[2][1] == couleur and tab[3][0] == couleur:
        alignement_de_4_pions = False
    elif tab[0][4] == couleur and tab[1][3] == couleur and tab[2][2] == couleur and tab[3][1] == couleur:
        alignement_de_4_pions = False
    elif tab[1][3] == couleur and tab[2][2] == couleur and tab[3][1] == couleur and tab[4][0] == couleur:
        alignement_de_4_pions = False
    elif tab[0][5] == couleur and tab[1][4] == couleur and tab[2][3] == couleur and tab[3][2] == couleur:
        alignement_de_4_pions = False
    elif tab[1][4] == couleur and tab[2][3] == couleur and tab[3][2] == couleur and tab[4][1] == couleur:
        alignement_de_4_pions = False
    elif tab[2][3] == couleur and tab[3][2] == couleur and tab[4][1] == couleur and tab[0][5] == couleur:
        alignement_de_4_pions = False
    elif tab[0][6] == couleur and tab[1][5] == couleur and tab[2][4] == couleur and tab[3][3] == couleur:
        alignement_de_4_pions = False
    elif tab[1][5] == couleur and tab[2][4] == couleur and tab[3][3] == couleur and tab[4][2] == couleur:
        alignement_de_4_pions = False
    elif tab[2][4] == couleur and tab[3][3] == couleur and tab[4][2] == couleur and tab[5][1] == couleur:
        alignement_de_4_pions = False
    elif tab[1][6] == couleur and tab[2][5] == couleur and tab[3][4] == couleur and tab[4][3] == couleur:
        alignement_de_4_pions = False
    elif tab[2][5] == couleur and tab[3][4] == couleur and tab[4][3] == couleur and tab[5][2] == couleur:
        alignement_de_4_pions = False
    elif tab[2][6] == couleur and tab[3][5] == couleur and tab[4][4] == couleur and tab[5][3] == couleur:
        alignement_de_4_pions = False
    return alignement_de_4_pions


def puissance4():
    tab = [['.', '.', '.', '.', '.', '.', '.'],
           ['.', '.', '.', '.', '.', '.', '.'],
           ['.', '.', '.', '.', '.', '.', '.'],
           ['.', '.', '.', '.', '.', '.', '.'],
           ['.', '.', '.', '.', '.', '.', '.'],
           ['.', '.', '.', '.', '.', '.', '.']]
    alignement_de_4_pions = True
    while alignement_de_4_pions:
        a = int(input("Dans quelle colonne voulez vous placer un pions. "))  # pour le joueur 1
        if a > 7:
            a = int(input("Votre nombre doit etre inferieur a 7. "))
        a = a - 1
        i, j = 0, 0
        pions_place = True
        while i <= 5 and pions_place:
            if tab[i][a] == '.':
                tab[i][a] = 'j'
                y = i
                pions_place = False
            else:
                i += 1
        pions_place = True
        longueur = a
        hauteur = y
        couleur = 'j'
        alignement_de_4_pions = f_verifcolonne(hauteur, longueur, alignement_de_4_pions, couleur, tab)
        alignement_de_4_pions = f_verifdiago(hauteur, longueur, alignement_de_4_pions, couleur, tab)
        alignement_de_4_pions = f_verifautrediago(hauteur, longueur, alignement_de_4_pions, couleur, tab)
        alignement_de_4_pions = f_verifligne(hauteur, longueur, alignement_de_4_pions, couleur, tab)
        if alignement_de_4_pions == False:
            print("le joueur jaune a gagne")
        pprint(list(reversed(tab)), indent=2)
        if alignement_de_4_pions != False:
            b = int(input("Dans quelle colonne voulez vous placer un pions. "))  # pour le joueur 2
            if b > 7:
                b = int(input("Votre nombre doit etre inferieur a 7. "))
            b = b - 1
            while j <= 5 and pions_place:
                if tab[j][b] == '.':
                    tab[j][b] = 'r'
                    x = j
                    pions_place = False
                else:
                    j += 1
            longueur = b
            hauteur = x
            couleur = 'r'
            alignement_de_4_pions = f_verifcolonne(hauteur, longueur, alignement_de_4_pions, couleur, tab)
            alignement_de_4_pions = f_verifdiago(hauteur, longueur, alignement_de_4_pions, couleur, tab)
            alignement_de_4_pions = f_verifautrediago(hauteur, longueur, alignement_de_4_pions, couleur, tab)
            alignement_de_4_pions = f_verifligne(hauteur, longueur, alignement_de_4_pions, couleur, tab)
            pprint(list(reversed(tab)), indent=2)
            if alignement_de_4_pions == False:
                print("le joueur rouge a gagne")


puissance4()
