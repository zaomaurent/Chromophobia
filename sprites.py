from constantes import *
from functions import Distance
from Sons import gun_sound

coef_angle_tailleX = tailleX / fov_r


def Sprite_calcul(sprite, player_x, player_y, HEIGHT, dist_list, last_shot, fov_moins, fov_plus, sp_pl_angle, sprite_x,
                  sprite_y, weapon, shot, damage,
                  dead_mobs):  # Fonction de calcul et d'affichage des sprites et de leurs coordonnées
    global TS, player_hp

    viewed_sprite = False  # Variable booléenne pour savoir si le sprite est visible par le personnage
    sprite_coord = [2000, 2000]  # Coordonnées si le sprite n'est pas visible pour qu'il soit affiché hors de l'écran

    if fov_moins <= sp_pl_angle <= fov_plus:  # Si le sprite se situe dans le champ de vision
        if sprite["class"] == "ennemy":  # Si le sprite est un ennemi
            if sprite["HP"] <= 0:  # Affiche le sprite mort allongé si ses points de vie sont en dessous de 0
                texture = sprite["dead_texture"]
            else:  # Affiche le sprite normalement si ses points de vie sont au dessus de 0
                texture = sprite["texture"]

            column = int(abs(coef_angle_tailleX * (sp_pl_angle - HALF_FOV)))

            sprite_distance = Distance(sprite_x - player_x, sprite_y - player_y) * m.cos(
                sp_pl_angle)  # Appel de la fonction calculant la distance du sprite

            if 15 < sprite_distance <= dist_list[
                int(column // LINE_SIZE)]:  # Si le sprite est devant un mur et à plus de 15 de distance (évite les bugs lorsque l'on traverse un sprite)
                sprite_height = int(((TS / 1.05) / sprite_distance) * SCREEN_DISTANCE)
                sprite_width = sprite_height * sprite["ratio"]
                scaled_sprite = pg.transform.scale(texture, (sprite_width, sprite_height))
                sprite_coord = (column - sprite_width // 2, (tailleY / 2) - (sprite_height // 2) + HEIGHT)
                screen.blit(scaled_sprite, sprite_coord)
                viewed_sprite = True
                sprite_attack(sprite_distance, sprite)

        else:
            column = int(abs(coef_angle_tailleX * (sp_pl_angle - HALF_FOV)))

            sprite_distance = Distance(sprite_x - player_x, sprite_y - player_y) * m.cos(sp_pl_angle)

            if 15 < sprite_distance <= dist_list[int(column // LINE_SIZE)]:
                sprite_height = int(((TS / 1.05) / sprite_distance) * SCREEN_DISTANCE)
                sprite_width = sprite_height * sprite["ratio"]
                scaled_sprite = pg.transform.scale(sprite["texture"], (sprite_width, sprite_height))
                sprite_coord = [column - sprite_width // 2, (tailleY / 2) - (sprite_height // 2) + HEIGHT]
                screen.blit(scaled_sprite, sprite_coord)
                viewed_sprite = True

    if shot:
        if sprite["class"] == "ennemy":
            if sprite["HP"] > 0:
                last_shot = t.time()

        gun_sound(weapons[weapon]["sound"], weapons[weapon]["volume"])

        if viewed_sprite:
            dead_mobs = attack(damage, sprite_width, sprite_width, sprite_coord, sprite, dead_mobs)

    return last_shot, dead_mobs


def Sprite_angle(player_x, player_y, sprite_x, sprite_y):
    base_angle = m.atan(abs(sprite_x - player_x) / abs(sprite_y - player_y))

    if player_x > sprite_x and player_y > sprite_y:
        return base_angle

    elif player_x > sprite_x and player_y < sprite_y:
        return m.radians(180) - base_angle

    elif player_x < sprite_x and player_y > sprite_y:
        return m.radians(360) - base_angle

    else:
        return m.radians(180) + base_angle


def Sprite(player_x, player_y, player_rotation, HEIGHT, dist_list, last_shot, weapon, sprites, reloading, dead_mobs):
    global TS, player_hp
    speed, damage = weapons[weapon]["speed"], weapons[weapon]["damage"]
    left, middle, right = pg.mouse.get_pressed()
    if left and t.time() - last_shot >= speed and not reloading and weapons[weapon]["mag"] > 0:
        shot = True
        weapons[weapon]["mag"] -= 1
    else:
        shot = False
    # Fonction pour afficher les sprites
    for sprite in sprites.values():
        sprite_x, sprite_y = sprite["position"]
        sprite_angle = Sprite_angle(player_x, player_y, sprite_x, sprite_y)
        sp_pl_angle = sprite_angle - player_rotation
        fov_plus, fov_moins = HALF_FOV, - HALF_FOV
        last_shot, dead_mobs = Sprite_calcul(sprite, player_x, player_y, HEIGHT, dist_list, last_shot, fov_moins,
                                             fov_plus,
                                             sp_pl_angle, sprite_x, sprite_y, weapon, shot, damage, dead_mobs)

    return last_shot, player_hp, dead_mobs


def draw_object(sprites, player_x, player_y, player_rotation):
    for sprite in sprites.values():
        if sprite["class"] == "ennemy":
            if sprite["HP"] > 0:
                pg.draw.circle(screen, (220, 50, 0), sprite["position"], 4)

    #  Joueur
    pg.draw.circle(screen, (255, 0, 0), (player_x, player_y), 4)
    pg.draw.line(screen, (255, 0, 0), (player_x, player_y),
                 (player_x - 25 * m.sin(player_rotation), player_y - 25 * m.cos(player_rotation)))


def attack(damage, sprite_width, sprite_height, sprite_coord, sprite, dead_mobs):
    global TS, player_hp

    limit_left, limit_right = sprite_coord[0], sprite_coord[0] + sprite_width
    limit_up, limit_down = sprite_coord[1], sprite_coord[1] + sprite_height

    if limit_left <= tailleX / 2 <= limit_right and limit_up <= tailleY / 2 <= limit_down and sprite["class"] == "ennemy":
        sprite_hp_before = sprite["HP"]
        sprite["HP"] -= damage
        if sprite_hp_before > 0 >= sprite["HP"]:
            player_hp += 50
            dead_mobs += 1

            if player_hp > 500:
                player_hp = 500

    return dead_mobs


def sprite_attack(sprite_distance, sprite):
    global player_hp
    if sprite["HP"] > 0 and t.time() - sprite["last_hit"] >= 2:
        player_hp -= 20
        sprite["last_hit"] = t.time()
        return player_hp
