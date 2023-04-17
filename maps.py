import pygame as pg

maps = {
    '1': {
        "map": [  # Liste représentant la map en 2D (un chiffre différent de zéro
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],  # correspond à l'emplacement d'un mur et à la texture qui lui est associée
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 5, 0, 5, 5, 0, 5],
            [5, 0, 0, 3, 3, 0, 5, 0, 0, 5],
            [5, 5, 0, 3, 0, 0, 0, 0, 5, 5],
            [5, 5, 0, 1, 0, 0, 0, 0, 5, 5],
            [5, 0, 0, 0, 0, 0, 5, 0, 0, 5],
            [5, 0, 5, 0, 5, 0, 5, 5, 0, 5],
            [5, 0, 0, 0, 5, 0, 0, 0, 0, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        ],
        "map size": 10,  # Taille de la map
        "tile size": 250 / 10,  # Echelle de la map
        "spawn point": (37.5, 37.5),  # Point d'apparition du joueur
        "sprites": {  # Dictionnaire des différents sprites et de leur position

            "1": {
                "texture": pg.image.load("Assets/Sprites/Ennemis/test.png"),  # Texture du sprite
                "height": 51,  # Hauteur de la texture
                "width": 37,  # Largeur de la texture
                "ratio": 37 / 51,  # Ratio de la hauteur et la largeur de la texture
                "position": (120, 120),  # Position du sprite
                "class": "ennemy",  # Classe du sprite (ennemi, neutre ou PNJ)
                "HP": 100,  # Points de vie du sprite si c'est un ennemi
                "dead_texture": pg.image.load("Assets/Sprites/Ennemis/test_death.png")  # Texture du sprite mort
            },

            "2": {
                "texture": pg.image.load("Assets/Sprites/Ennemis/test.png"),
                "height": 51,
                "width": 37,
                "ratio": 37 / 51,
                "position": (210, 210),
                "class": "ennemy",
                "HP": 100,
                "dead_texture": pg.image.load("Assets/Sprites/Ennemis/test_death.png")
            },

            "3": {
                "texture": pg.image.load("Assets/Sprites/greenlight.png"),
                "height": 96,
                "width": 64,
                "ratio": 64 / 96,
                "position": (37, 37),
                "class": "neutral"
            },

            "4": {
                "texture": pg.image.load("Assets/Sprites/greenlight.png"),
                "height": 96,
                "width": 64,
                "ratio": 64 / 96,
                "position": (0, 0),
                "class": "PNJ"
            },

            "5": {
                "texture": pg.image.load("Assets/Sprites/Ennemis/test.png"),  # Texture du sprite
                "height": 51,
                "width": 37,
                "ratio": 37 / 51,
                "position": (140, 140),
                "class": "ennemy",
                "HP": 100,
                "dead_texture": pg.image.load("Assets/Sprites/Ennemis/test_death.png")
            },
        }
    },

    '2': {
        "map": [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ],
        "map size": 3,
        "tile size": 250 / 3,  # 250/map size
        "spawn point": (250 / 3, 250 / 3),
        "sprites": {
            "1": {
                "texture": pg.image.load("Assets/Sprites/Ennemis/test.png"),
                "height": 51,
                "width": 37,
                "ratio": 37 / 51,
                "position": (50, 50),
                "class": "ennemy",
                "HP": 100,
                "dead_texture": pg.image.load("Assets/Sprites/Ennemis/test_death.png")
            },

        }, },

    '3': {
        "map":
            [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
              4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
              4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
              4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
              4, 4, 4, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
              4, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
              0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0,
              0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0,
              0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0,
              0, 4, 4, 4, 0, 0, 4, 4, 0, 0, 0, 0, 0, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0,
              0, 4, 4, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0,
              0, 4, 0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0, 0, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0,
              0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 4, 0, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 0, 4, 0, 4, 0, 0, 0, 4, 0, 4, 4, 4, 0,
              0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 4, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0,
              0, 0, 4, 4, 0, 0, 4, 4, 4, 0, 0, 4, 0, 0, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 0, 0,
              0, 0, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 0, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 4, 4, 0, 0, 4, 4, 4, 4, 4, 0, 4, 4, 4, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 4, 4, 4, 4,
              4, 4, 4, 4, 0, 0, 0, 4, 0, 0, 0, 0, 4, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4,
              0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 4, 4, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0,
              0, 0, 0, 4, 4, 0, 4, 0, 0, 0, 4, 4, 4, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0,
              4, 0, 0, 4, 4, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0,
              4, 4, 0, 4, 4, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 0, 0, 4, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0,
              0, 0, 0, 4, 4, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 0, 0, 4, 0, 4, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 4, 4, 4, 4,
              4, 4, 4, 4, 4, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, 4, 0, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4,
              4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 0, 0, 4, 0, 4, 0, 4, 0, 0, 0, 0, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4,
              0, 0, 4, 4, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 4, 0, 4, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 4, 0, 0, 4, 4,
              0, 0, 4, 0, 0, 4, 4, 0, 0, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 4, 0, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 4,
              0, 0, 4, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0, 4, 0, 0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4,
              4, 0, 0, 0, 4, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 4, 0, 4, 0, 0, 4, 0, 4, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4,
              4, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 0, 0, 0, 4, 4, 0, 0, 0, 0, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0, 0, 0, 4, 4,
              4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 4, 0, 0, 0, 4, 0, 0, 0, 4, 4, 0, 4, 4, 4, 4, 0, 4, 4, 4, 0, 0, 0, 0, 4, 0, 4, 4, 0, 0, 0, 0, 0, 4,
              4, 0, 0, 0, 4, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 0, 4, 0, 4, 0, 4, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 4,
              4, 0, 0, 0, 4, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, ],
             [4, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 4, 4, 4, 0, 0, 0, 4, 4,
              4, 4, 4, 4, 4, 0, 4, 4, 0, 4, 4, 4, 4, 4, 4, ],
             [4, 0, 0, 0, 4, 0, 4, 0, 0, 4, 0, 4, 0, 4, 0, 0, 0, 4, 0, 0, 4, 4, 0, 4, 4, 0, 0, 4, 4, 4, 4, 0, 4, 4, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, ],
             [4, 0, 4, 0, 4, 0, 0, 0, 0, 4, 4, 4, 0, 4, 4, 4, 4, 4, 0, 0, 4, 4, 0, 0, 0, 0, 0, 4, 4, 4, 4, 0, 4, 4, 0,
              0, 4, 0, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 0, 4, 0, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 0,
              4, 4, 0, 0, 4, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0, 4, 4, 0, 4, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 0,
              0, 0, 0, 4, 4, 4, 4, 0, 0, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 4, 4, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 4, 0,
              0, 0, 0, 4, 4, 4, 4, 0, 0, 4, 4, 4, 4, 4, 4, ],
             [4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 4, 0,
              4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 0, 0, 0, 4, 0, 0, 0, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 4, 4, 0, 0, 4, 4, 4, 0, 0, 4, 4, 0, 0, 4, 4, 4, 0,
              0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 0, 0, 4, 4, 4, 4, 0, 4, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0,
              0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 4, 4,
              4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 0, 0, 4, 4, 0, 0, 0, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4,
              4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 0, 0, 4, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4,
              4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 0, 0, 0, 0, 4, 4, 4, 0, 4, 0, 4, 0, 0, 0, 4, 0, 0, 4, 0, 0, 4, 4, 4, 4, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4,
              4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 4, 0, 0, 4, 4, 0, 0, 4, 4, 4, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4,
              4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4,
              4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 4, 4, 4, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4,

          4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ],
             [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
              4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, ]],
        "map size": 50,
        "tile size": 250 / 50,
        "spawn point": (25.5 * 5, 47.5 * 5),
        "sprites": {
            "1": {
                "texture": pg.image.load("Assets/Sprites/greenlight.png"),
                "height": 96,
                "width": 64,
                "ratio": 64 / 96,
                "position": (25.5 * 5, 48 * 5),
                "class": "neutral"
            }
        }
    }
}

