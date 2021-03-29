import pygame

#classe boule de feu magique
class magie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity=13
        self.image=pygame.image.load('assets/jp.jpeg')
        self.rect=self.image.get_rect()


