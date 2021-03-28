import pygame


# creation 1er classe joueur
class Player(pygame.sprite.Sprite):
    def __init__(self):
        infoEcran = pygame.display.Info()
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 14
        self.velocityJump = 10
        self.image = pygame.image.load("design\Wizard\PNG\Wizard_fire\idle_2.png")
        # adaptation pour que mage1 puisse s'adapter à tout écran
        self.image = pygame.transform.scale(self.image, (infoEcran.current_w // 5, infoEcran.current_h // 3))
        # position de départ du joueur 1
        self.rect = self.image.get_rect()
        self.rect.x = infoEcran.current_w // 9
        self.rect.y = infoEcran.current_h // 1.55

    def move_right(self):
        self.rect.x+=self.velocity

    def move_left(self):
        self.rect.x-=self.velocity

    def jump(self):
        infoEcran = pygame.display.Info()
        if infoEcran.current_h // 1.55 == self.rect.y:
            self.rect.y-=self.velocity
