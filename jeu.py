import pygame
from player import Player


# classe qui représente jeu
class Jeu:
    def __init__(self):
        self.player = Player()
        self.pressed={}