import pygame
from magie import Magie

# creation 1er classe joueur
class Player_red(pygame.sprite.Sprite):
    def __init__(self, jeu):
        super().__init__()
        #on utilise les selfs pour que les variables puissent etre utilisés dans toute la classe
        self.jeu = jeu
        self.infoEcran = pygame.display.Info()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.all_projectiles = pygame.sprite.Group()
        self.velocity = 12
        self.jumping = False
        self.velocity_jumpMax = 25
        self.velocity_jump = self.velocity_jumpMax
        self.image = pygame.image.load("design\Wizard\PNG\Wizard_fire\idle_2.png")
        # adaptation pour que mage1 puisse s'adapter à tout écran
        self.image = pygame.transform.scale(self.image, (self.infoEcran.current_w // 5, self.infoEcran.current_h // 3))
        # position de départ du joueur 1
        self.rect = self.image.get_rect()
        self.rect.x = self.infoEcran.current_w // 9
        self.rect.y = self.infoEcran.current_h // 1.55

    def damage (self, quantité ):
        #infliger des degats
        self.health-=quantité

    def maj_barre_vie (self,surface):
        #couleur pour jauge de vie
        couleur_barre =(124, 233, 146) #verte

        # couleur arriere plan de jauge
        fond_couleur_barre = (186, 216, 186)  # gris

        #position jauge de vie plus taille
        position_barre=[self.rect.x+(self.infoEcran.current_w//22.5),self.rect.y-(self.infoEcran.current_h//120), self.health, 10] #self.health est la longueur de la barre , epaisseur

        # position arriere plan jauge
        arriere_plan_position =[self.rect.x+(self.infoEcran.current_w//22.5),self.rect.y-(self.infoEcran.current_h//120), self.max_health, 10] # self.max_health est la longueur totale de la barre , epaisseur

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

    def jump(self):
        self.rect.y -= self.velocity_jump
        self.velocity_jump -= 1
        if self.velocity_jump < -self.velocity_jumpMax:
            self.jumping = False
            self.velocity_jump = self.velocity_jumpMax
