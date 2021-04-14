import pygame

class Magie(pygame.sprite.Sprite):
    def __init__(self, player, flipped):
        infoEcran = pygame.display.Info()
        self.ecranW = infoEcran.current_w
        self.player = player
        super().__init__()
        self.magie_turn = 0
        self.velocity=13
        self.image=pygame.image.load('design\jp.jpeg')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect=self.image.get_rect()
        if not flipped:
            self.rect.x = player.rect.x + (self.ecranW // 6.2)
            self.rect.y = player.rect.y + (self.ecranW // 10)
        else:
            self.rect.x = player.rect.x + (self.ecranW // 50)
            self.rect.y = player.rect.y + (self.ecranW // 10)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self, flipped):
            if not flipped and self.magie_turn == 0 or self.magie_turn == 1:
                self.rect.x += self.velocity
                self.magie_turn = 1
            elif flipped and self.magie_turn == 0 or self.magie_turn == 2:
                self.rect.x -= self.velocity
                self.magie_turn = 2
            if self.rect.x > self.ecranW or self.rect.x < 0:
                self.remove()



