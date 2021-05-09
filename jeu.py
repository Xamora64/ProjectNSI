import pygame
from player_red import Player_red
from player_purple import Player_purple


# classe qui représente jeu
class Jeu:
    def __init__(self):
        self.player_red = Player_red(self)
        self.player_purple = Player_purple(self)
        self.pressed={}

    #Permet de géré les colission surtout des boules de feu sur le joueur, le True permet de dire que sa se supprime
    #On prend un sprite, un group, un boolean, et créer une "hitbox"
    #Le sprite est unique telle un joueur, un groupe de sprite telle les boules de feu, le boolean pour savoir si
    #un élement du groupe se supprime en touchant le spirte, et la hitbox pour savoir quand sa touche
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)



