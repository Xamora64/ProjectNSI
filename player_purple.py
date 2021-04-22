import pygame
from magie import Magie

# creation 1er classe joueur
class Player_purple(pygame.sprite.Sprite):
    def __init__(self, jeu):
        super().__init__()
        self.sprite = pygame.sprite.Sprite
        self.jeu = jeu
        self.infoEcran = pygame.display.Info()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.all_projectiles = pygame.sprite.Group()
        self.velocity = 10
        self.image = pygame.image.load("design\Wizard\PNG\Wizard\idle_1.png")
        # adaptation pour que mage1 puisse s'adapter à tout écran
        self.image = pygame.transform.scale(self.image, (int(self.infoEcran.current_w / 5.5), int(self.infoEcran.current_h // 3.3)))
        #Fait "flip" l'image à 90 degres pour regarder à gauche
        #self.image = pygame.transform.flip(self.image, 90, 0)
        # position de départ du joueur 1
        self.rect = self.image.get_rect()
        self.rect.x = self.infoEcran.current_w // 1.5
        self.rect.y = self.infoEcran.current_h // 1.48

    def damage (self, quantité ):
        #infliger des degats0
        self.health-=quantité
        #if self.health <= 0:
            #faire la mort

    def maj_barre_vie (self,surface):
        #couleur pour jauge de vie

        couleur_barre = (124, 233, 146)  # verte

        #couleur arriere plan de jauge
        fond_couleur_barre =(186, 216, 186) #gris

        #position jauge de vie plus taille
        position_barre=[self.rect.x+(self.infoEcran.current_w//20.5),self.rect.y-(self.infoEcran.current_h//120), self.health, 10] #self.health est la longueur de la barre , epaisseur

        #position arriere plan jauge
        arriere_plan_position =[self.rect.x+(self.infoEcran.current_w//20.5),self.rect.y-(self.infoEcran.current_h//120), self.max_health, 10] #self.max_health est la longueur totale de la barre , epaisseur

        #apparition barre de vie
        pygame.draw.rect(surface, fond_couleur_barre,arriere_plan_position)
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

