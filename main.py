import pygame
pygame.init()

#classe qui représente jeu
class Jeu():
    def _init_(self):
        self.player =Player()

#creation 1er classe joueur

class Player(pygame.sprite.Sprite):
    def _init_(self):
        super._init_()
        self.health=100
        self.max_health=100
        self.attack=5
        self.velocity=6
        self.image=pygame.image.load("design\2D-Game-Wizard-Character-Sprite\PNG\wizard_fire\idle_2.png") #attention relire
#position de départ du joueur 1
        self.rect=self.image.get_rect()
        self.rect.x=450
        self.rect.y=500


# générer la fenetre de notre jeu
pygame.display.set_caption("Mage")

# Info de la taille de l'écran de l'utilisateur
infoEcran = pygame.display.Info()
ecran = pygame.display.set_mode((infoEcran.current_w, infoEcran.current_h))

# importer l'image pour l'arrière plan du jeu
fondEcran = pygame.image.load("design\cartoonFantasticBackground\PNG\Cartoon_Forest_BG_04\Foret_1.png")
fondEcran = pygame.transform.scale(fondEcran, (infoEcran.current_w, infoEcran.current_h))

#creat° variable, chargement arriere plan
jeu=Jeu()

enFonctionnement = True

# boucle tant que running est vrai
while enFonctionnement:

    # appliquer l'arriere plan du jeu
    ecran.blit(fondEcran,(0, 0))

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
