import pygame
from jeu import Jeu

pygame.init()

# générer la entre de notre jeu
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
