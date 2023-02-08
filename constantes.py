import pygame as pg
import math as m

from maps import maps
from players import players


# Appel de fonctions
map_number = 1
map = maps[map_number]
TS = map["tile size"]
tailleX, tailleY = 1600, 800  # Taille de l'écran en x et y (width et height)
running = True

pg.init()
screen = pg.display.set_mode((tailleX, tailleY))
pg.display.set_caption("Raycasting")

# Parametres variables pour le joueur

fov_d = 80  # Champ de vision en radians
fov_r = m.radians(fov_d)  # Champ de vision en radians
HALF_FOV = fov_r / 2
mouse_speed = 1  # Sensibilité de la souris lors du mouvement
mouse_coef = m.radians(90) * (mouse_speed / tailleX)  # --> Coeficient utilisé lors de du mouvement de la souris
crosshair_path = "Assets/crosshair.png"  # Permet au joueur de choisir son viseur
crosshair = pg.image.load(crosshair_path)
crosshair_size = 3  # Taille du viseur
max_check = 6 # --> Distance d'affichage maximale


# Constantes

# Pour le joueur
player = players[1]
player_x, player_y = player["spawn"]
player_rotation = player["base rotation"]
speed = 1 * TS / 25  # vitesse de base du joueur
current_speed = speed  # deuxieme variable afin de pouvoir courir

# Pour le Raycaster
LINE_SIZE = 4  # Le raycaster fonctionne par colonne qu'il affiche, LINE_SIZE est la taille en pixel de ces colonnes
nb_LINE = tailleX / LINE_SIZE  # Nombre de rayons envoyés == nombre de colonnes affichées sur l'écran
RAY_SENSI = fov_r / nb_LINE  # Angle entre chaque rayon du raycaster
MAX_DEPTH = TS * max_check  # En fonction de la distance d'affichages, c'est la taille maximum d'un rayon

# Pour l'affichage des colonnes
SCREEN_DISTANCE = int((tailleX / 2) / m.tan(HALF_FOV))  # On utilise le théoreme de thales et la trigo pour calculer
# la taille en pixel d'un mur en fonction de sa distance au joueur
calc_auxiliary = SCREEN_DISTANCE * TS  # Allège les calcul pour ceux de la taille d'un mur en pixel

# Pour le crosshair ou autres
MID_POINT = (tailleX / 2, tailleY / 2)  # Calcul le milieu de l'ecran
C_w, C_h = crosshair.get_size()  # Crossair_width, crosshair_height
C_w, C_h = crosshair_size * C_w, crosshair_size * C_h  # On redimentionne sa taille a la taille voulue par l'utilisateur
Crosshair = pg.transform.scale(crosshair, (C_w, C_h))  # Puis on scale l'objet pygame
Crosshair_coord = (MID_POINT[0] - m.floor(C_w / 2), MID_POINT[1] - m.floor(C_h / 2))  # Calcul de la bonne position

# Initialisation des textures

wall_textures = [  # Chaque element a pour forme (objet pygame du la texture, résolution de la texture)
    (pg.image.load("Assets/walls/wall.png").convert(), 32),
    (pg.image.load("Assets/walls/wall_test.png").convert(), 64),
    (pg.image.load("Assets/walls/wall2.png").convert(), 128),
    (pg.image.load("Assets/walls/wall_vent.png").convert(), 564),
    (pg.image.load("Assets/walls/blue_wall.png").convert(), 225)

]
background = pg.image.load("Assets/GUI/background.png").convert()  # image de fond du menu d'accueil




# Autres
MAP_SIZE = map["map size"]
WDW_SIZE = TS * MAP_SIZE  # Combien de place prend la map en pixel
HEIGHT = 0  # Variable pour definir la hauteur de la souris, permet de regarder en bas et en haut
angle = m.radians(90)  # pour alléger le code lors de calcul du deplacement droite/gauche
mouse = pg.mouse
clock = pg.time.Clock()

