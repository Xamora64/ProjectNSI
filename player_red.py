import pygame
from magie import Magie

# creation 1er classe joueur
class Player_red(pygame.sprite.Sprite):
    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        infoEcran = pygame.display.Info()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.all_projectiles = pygame.sprite.Group()
        self.velocity = 10
        self.image = pygame.image.load("design\Wizard\PNG\Wizard_fire\idle_2.png")
        # adaptation pour que mage1 puisse s'adapter à tout écran
        self.image = pygame.transform.scale(self.image, (infoEcran.current_w // 5, infoEcran.current_h // 3))
        # position de départ du joueur 1
        self.rect = self.image.get_rect()
        self.rect.x = infoEcran.current_w // 9
        self.rect.y = infoEcran.current_h // 1.55

    def damage (self, quantité ):
        #infliger des degats
        self.health-=quantité

    def maj_barre_vie (self,surface):
        #couleur pour jauge de vie
        couleur_barre =(124, 233, 146) #verte

        # couleur arriere plan de jauge
        fond_couleur_barre = (186, 216, 186)  # gris

        #position jauge de vie plus taille
        position_barre=[self.rect.x+50,self.rect.y-5, self.health, 10] #self.health est la longueur de la barre , epaisseur

        # position arriere plan jauge
        arriere_plan_position = [self.rect.x +50, self.rect.y -5, self.max_health,10]  # self.max_health est la longueur totale de la barre , epaisseur

        #apparition barre de vie
        pygame.draw.rect(surface, fond_couleur_barre, arriere_plan_position)
        pygame.draw.rect(surface,couleur_barre,position_barre)



    def launch_Magie(self, flipped):
        # creation d'une nouvelle instance magie pour cloner l'attaque magique
        self.all_projectiles.add(Magie(self, flipped))

    def move_right(self, flipped):
        self.rect.x+=self.velocity
        if flipped == True:
            self.image=pygame.transform.flip(self.image,90,0)

    def move_left(self, flipped):
        self.rect.x-=self.velocity
        if flipped == False:
            self.image=pygame.transform.flip(self.image,-90,0)
