import pygame
from magie import Magie

# creation 1er classe joueur
class Player_purple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        infoEcran = pygame.display.Info()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.all_projectiles = pygame.sprite.Group()
        self.velocity = 10
        self.image = pygame.image.load("design\Wizard\PNG\Wizard\idle_1.png")
        # adaptation pour que mage1 puisse s'adapter à tout écran
        self.image = pygame.transform.scale(self.image, (int(infoEcran.current_w / 5.5), int(infoEcran.current_h // 3.3)))
        # position de départ du joueur 1
        self.rect = self.image.get_rect()
        self.rect.x = infoEcran.current_w // 7
        self.rect.y = infoEcran.current_h // 1.48

    def maj_barre_vie (self,surface):
        #couleur pour jauge de vie
        couleure_barre =(139, 246, 161) #verte

        #position jauge de vie plus taille
        position_barre=[self.rect.x,self.rect.y, self.health, 10] #self.health est la longueur de la barre , epaisseur

        #apparition barre de vie
        pygame.draw.rect(surface,couleure_barre,position_barre)

    def launch_Magie(self):
        # creation d'une nouvelle instance magie pour cloner l'attaque magique
        self.all_projectiles.add(Magie(self))

    def move_right(self, flipped):
        self.rect.x+=self.velocity
        if flipped == True:
            self.image=pygame.transform.flip(self.image,90,0)

    def move_left(self, flipped):
        self.rect.x-=self.velocity
        if flipped == False:
            self.image=pygame.transform.flip(self.image,-90,0)

