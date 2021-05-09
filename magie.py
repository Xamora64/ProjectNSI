import pygame

class Magie(pygame.sprite.Sprite):
    def __init__(self, player, flipped):
        infoEcran = pygame.display.Info()
        self.ecranW = infoEcran.current_w
        self.player = player
        super().__init__()
        self.magie_turn = 0
        self.velocity=20
        if player == self.player.jeu.player_red:
            self.image = pygame.image.load("design/Boule/BouleRouge.png")
        else:
            self.image = pygame.image.load("design/Boule/BouleViolet.png")
        self.image = pygame.transform.scale(self.image, (self.ecranW // 20, self.ecranW // 20))
        self.rect=self.image.get_rect()
        if not flipped:
            self.rect.x = player.rect.x + (self.ecranW // 6.2)
            self.rect.y = player.rect.y + (self.ecranW // 10)
        else:
            self.rect.x = player.rect.x - (self.ecranW //50)
            self.rect.y = player.rect.y + (self.ecranW // 10)


    def move(self, flipped):
            if self.player.jeu.check_collision(self.player.jeu.player_red,self.player.all_projectiles) or self.player.jeu.check_collision(self.player.jeu.player_purple,self.player.all_projectiles):
                #supprime la boule quand elle touche un joueur
                if self.player != self.player.jeu.player_red:
                    self.player.jeu.player_red.damage(20)
                    self.player.jeu.player_purple.magie = self.player.jeu.player_purple.magie + 1
                elif self.player != self.player.jeu.player_purple:
                    self.player.jeu.player_purple.damage(20)
                    self.player.jeu.player_red.magie = self.player.jeu.player_red.magie + 1


            if not flipped and self.magie_turn == 0 or self.magie_turn == 1:
                self.rect.x += self.velocity
                self.magie_turn = 1
            elif flipped and self.magie_turn == 0 or self.magie_turn == 2:
                self.rect.x -= self.velocity
                self.magie_turn = 2
            if self.rect.x > self.ecranW or self.rect.x < 0:
                self.player.all_projectiles.remove(self)
                if self.player == self.player.jeu.player_red:
                    self.player.jeu.player_red.magie = self.player.jeu.player_red.magie + 1
                    self.player.jeu.player_purple.damage(0)
                else:
                    self.player.jeu.player_purple.magie = self.player.jeu.player_purple.magie + 1
                    self.player.jeu.player_red.damage(0)




