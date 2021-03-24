import os

import pygame

pygame.init()


# classe qui représente jeu
class Jeu:
    def __init__(self):
        self.player = Player()


# creation 1er classe joueur

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 6
        self.image = pygame.image.load("design\Wizard\PNG\Wizard_fire\idle_2.png")  # attention relire design\2D-Game-Wizard-Character-Sprite\PNG\wizard_fire\idle_2.png
        # position de départ du joueur 1
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 1000


# générer la fenetre de notre jeu
pygame.display.set_caption("Mage")

# Info de la taille de l'écran de l'utilisateur
infoEcran = pygame.display.Info()
ecran = pygame.display.set_mode((infoEcran.current_w, infoEcran.current_h))

# importer l'image pour l'arrière plan du jeu
fondEcran = pygame.image.load("design\cartoonFantasticBackground\PNG\Cartoon_Forest_BG_04\Foret_1.png")
fondEcran = pygame.transform.scale(fondEcran, (infoEcran.current_w, infoEcran.current_h))

# Charger notre jeu
jeu = Jeu()

enFonctionnement = True

# boucle tant que running est vrai
while enFonctionnement:

    # appliquer l'arriere plan du jeu
    ecran.blit(fondEcran, (0, 0))

    # apparaitre mage
    ecran.blit(jeu.player.image, jeu.player.rect)

    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # dès que l'évenement "fermeture" est la
        if event.type == pygame.QUIT:
            enFonctionnement = False
            pygame.quit()
