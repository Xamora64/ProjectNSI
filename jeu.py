import pygame
from player_red import Player_red
from player_purple import Player_purple


# classe qui représente jeu
class Jeu:
    def __init__(self):
        self.player_red = Player_red(self)
        self.player_purple = Player_purple(self)
        self.pressed={}

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)



