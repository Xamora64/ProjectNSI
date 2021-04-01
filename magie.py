import pygame

#classe boule de feu magique
class Magie(pygame.sprite.Sprite):
    def __init__(self, player):
        infoEcran = pygame.display.Info()
        super().__init__()
        self.velocity=13
        self.image=pygame.image.load('design\jp.jpeg')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect=self.image.get_rect()
        self.rect.x = player.rect.x + (infoEcran.current_w//6.2)
        self.rect.y = player.rect.y + (infoEcran.current_w//10)

    def move(self):
        self.rect.x += self.velocity
