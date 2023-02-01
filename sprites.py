from constantes import *
from functions import Distance, Verif_Angle

sprites = {
    "1": {
        "texture": pg.image.load("Assets/Sprites/Ennemis/test.png").convert(),
        "height": 51,
        "width": 37,
        "ratio": 37 / 51,
        "position": (120, 120)
    }
}
coef_angle_tailleX = tailleX / fov_r


def Sprite(player_rotation, HEIGHT):
    # Fonction pour afficher les sprites
    for sprite in sprites.values():

        sprite_angle = m.radians(Verif_Angle((m.degrees(player_rotation) + 180) % 360, "deg"))
        fov_plus, fov_moins = Verif_Angle(player_rotation + HALF_FOV, "rad"), Verif_Angle(player_rotation - HALF_FOV,
                                                                                          "rad")
        print(m.degrees(fov_moins), m.degrees(sprite_angle), m.degrees(fov_plus))
        # Angle opposé au joueur
        if fov_moins > sprite_angle > fov_plus:
            print("oui")
            column = coef_angle_tailleX * (sprite_angle - player_rotation - HALF_FOV)
            sprite_x, sprite_y = sprite["position"]
            sprite_distance = Distance(sprite_x - player_x, sprite_y - player_y)
            if sprite_distance > 1:
                sprite_height = int(((TS / 1) / sprite_distance) * SCREEN_DISTANCE)
            else:
                sprite_height = tailleY
            sprite_width = sprite_height * sprite["ratio"]
            scaled_sprite = pg.transform.scale(sprite["texture"], (sprite_width, sprite_height))
            screen.blit(scaled_sprite, (column, (tailleY / 2) - (sprite_height // 2) + HEIGHT))
