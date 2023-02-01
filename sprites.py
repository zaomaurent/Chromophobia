from constantes import *
from functions import Distance, Verif_Angle

sprites = {
    "1": {
        "texture": pg.image.load("Assets/Sprites/Ennemis/test.png"),
        "height": 51,
        "width": 37,
        "ratio": 37 / 51,
        "position": (50, 50)
    }
}
coef_angle_tailleX = tailleX / fov_r

def Sprite_angle(player_x,player_y,sprite_x,sprite_y):
    base_angle = m.atan(abs(sprite_x - player_x) / abs(sprite_y - player_y))

    if player_x > sprite_x and player_y > sprite_y:
        return base_angle

    elif player_x > sprite_x and player_y < sprite_y:
        return m.radians(180) - base_angle

    elif player_x < sprite_x and player_y > sprite_y:
        return m.radians(360) - base_angle

    elif player_x < sprite_x and player_y < sprite_y:
        return m.radians(180) + base_angle


def Sprite(player_x,player_y,player_rotation, HEIGHT, dist_list):
    # Fonction pour afficher les sprites
    for sprite in sprites.values():
        sprite_x, sprite_y = sprite["position"]
        sprite_angle = Sprite_angle(player_x,player_y,sprite_x,sprite_y)
        sp_pl_angle = sprite_angle - player_rotation
        fov_plus, fov_moins = HALF_FOV, - HALF_FOV

        # Angle opposé au joueur

        if fov_moins <= sp_pl_angle <= fov_plus:

            column = int(abs(coef_angle_tailleX * (sp_pl_angle - HALF_FOV)))
            print(column)

            sprite_distance = Distance(sprite_x - player_x, sprite_y - player_y)

            if sprite_distance <= dist_list[int(column//LINE_SIZE)] :
                if sprite_distance > 1:
                    sprite_height = int(((TS / 1) / sprite_distance) * SCREEN_DISTANCE)
                else:
                    sprite_height = tailleY

                sprite_width = sprite_height * sprite["ratio"]
                scaled_sprite = pg.transform.scale(sprite["texture"], (sprite_width, sprite_height))
                screen.blit(scaled_sprite, (column - sprite_width//2, (tailleY / 2) - (sprite_height // 2) + HEIGHT))
