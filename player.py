import pygame

# creation 1er classe joueur

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 6
        self.image = pygame.image.load("design\Wizard\PNG\Wizard_fire\idle_2.png")
        #adaptation pour que mage1 puisse s'adapter à tout écran
        self.image = pygame.transform.scale(self.image, (infoEcran.current_w //5, infoEcran.current_h//3))
        # position de départ du joueur 1
        self.rect = self.image.get_rect()
        self.rect.x =infoEcran.current_w//9
        self.rect.y =infoEcran.current_h//1.55