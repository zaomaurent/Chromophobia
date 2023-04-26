import pygame as pg
import math as m
import time as t

from maps import maps

pg.init()
pg.mixer.init()

# Appel de fonctions
map_number = '1'
map = maps[map_number]
TS = map["tile size"]
tailleX, tailleY = 1600, 800  # Taille de l'écran en x et y (width et height)
running = True

screen = pg.display.set_mode((tailleX, tailleY))
pg.display.set_caption("Raycasting")

# Parametres variables pour le joueur

fov_d = 110  # Champ de vision en radians
fov_r = m.radians(fov_d)  # Champ de vision en radians
HALF_FOV = fov_r / 2
mouse_speed = 1  # Sensibilité de la souris lors du mouvement
mouse_coef = m.radians(90) * (mouse_speed / tailleX)  # --> Coeficient utilisé lors de du mouvement de la souris
crosshair_path = "Assets/crosshair.png"  # Permet au joueur de choisir son viseur
crosshair = pg.image.load(crosshair_path)
crosshair_size = 3  # Taille du viseur
max_check = 10  # --> Distance d'affichage maximale

# Constantes

# Pour le joueur
spawn_point = maps[map_number]["spawn point"]
players = {
    1: {
        "name": "Daniel",
        "spawn": spawn_point,
        "base rotation": m.radians(215)
    }
}
player = players[1]
player_x, player_y = player["spawn"]
player_rotation = player["base rotation"]
player_hp = 500
speed = 0.5  # vitesse de base du joueur
current_speed = speed  # deuxieme variable afin de pouvoir courir

# Pour le Raycaster
LINE_SIZE = 4 # Le raycaster fonctionne par colonne qu'il affiche, LINE_SIZE est la taille en pixel de ces colonnes
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
wall_color = 0  # 0 = rouge ; 1 = vert ; 2 = bleu ; 3 = gris
wall_textures = [  # Chaque element a pour forme (objet pygame du la texture, résolution de la texture)
    [
        (pg.image.load("Assets/walls/Rouge/blue_wall_rouge.png").convert(), 225),
        (pg.image.load("Assets/walls/Rouge/wall_rouge.png").convert(), 32),
    ],
    [
        (pg.image.load("Assets/walls/Vert/blue_wall_vert.png").convert(), 225),
        (pg.image.load("Assets/walls/Vert/wall_vert.png").convert(), 32),
    ],
    [
        (pg.image.load("Assets/walls/Bleu/blue_wall.png").convert(), 225),
        (pg.image.load("Assets/walls/Bleu/wall_bleu.png").convert(), 32),
    ],
    [
        (pg.image.load("Assets/walls/Gris/blue_wall_gris.png").convert(), 225),
        (pg.image.load("Assets/walls/Gris/wall_gris.png").convert(), 32),
    ],

]
background = pg.image.load("Assets/GUI/background.png").convert()  # image de fond du menu d'accueil

# Autres
MAP_SIZE = map["map size"]
WDW_SIZE = TS * MAP_SIZE  # Combien de place prend la map en pixel
HEIGHT = 0  # Variable pour definir la hauteur de la souris, permet de regarder en bas et en haut
angle = m.radians(90)  # pour alléger le code lors de calcul du deplacement droite/gauche
mouse = pg.mouse
clock = pg.time.Clock()

weapons = {
    1: {
        "speed": 0.05,
        "damage": 10,
        "sound": pg.mixer.Sound("Assets/Sons/blaster.ogg"),
        "name": "blaster",
        "volume": 0.25,
        'texture': pg.transform.scale(pg.image.load("Assets/blaster.png"), (300,300)),
        "coord": (tailleX - 300, tailleY - 200),
        "mag": 25,
        "max_mag": 25
    },

    2: {
        "speed": 1,
        "damage": 50,
        "sound": pg.mixer.Sound("Assets/Sons/gun.ogg"),
        "name": "gun",
        "volume": 0.3,
        'texture': pg.transform.scale(pg.image.load("Assets/gun.png"), (370,300)),
        "coord": (tailleX-370, tailleY - 300),
        "mag": 5,
        "max_mag": 5
    }
}


weapon = 1
last_shot = t.time()
reload_start = t.time()
reloading = False
dead_mobs = 0
