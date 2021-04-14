import pygame

class Magie(pygame.sprite.Sprite):
    def __init__(self, player, flipped):
        infoEcran = pygame.display.Info()
        super().__init__()
        self.magie_turn = 0
        self.velocity=13
        self.image=pygame.image.load('design\jp.jpeg')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect=self.image.get_rect()
        if not flipped:
            self.rect.x = player.rect.x + (infoEcran.current_w // 6.2)
            self.rect.y = player.rect.y + (infoEcran.current_w // 10)
        else:
            self.rect.x = player.rect.x + (infoEcran.current_w // 50)
            self.rect.y = player.rect.y + (infoEcran.current_w // 10)


    def move(self, flipped):
        print(self.magie_turn)
        if not flipped and self.magie_turn == 0 or self.magie_turn == 1:
            self.rect.x += self.velocity
            self.magie_turn = 1
        elif flipped and self.magie_turn == 0 or self.magie_turn == 2:
            self.rect.x -= self.velocity
            self.magie_turn = 2


