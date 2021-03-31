import pygame
from jeu import Jeu

pygame.init()

# générer la entre de notre jeu
pygame.display.set_caption("Mage")

# Info de la taille de l'écran de l'utilisateur
infoEcran = pygame.display.Info()
ecran = pygame.display.set_mode((int(infoEcran.current_w/1.35), int(infoEcran.current_h/1.35)))

# importer l'image pour l'arrière plan du jeu
fondEcran = pygame.image.load("design\cartoonFantasticBackground\PNG\Cartoon_Forest_BG_04\Foret_1.png")
fondEcran = pygame.transform.scale(fondEcran, (int(infoEcran.current_w/1.35), int(infoEcran.current_h/1.35)))

# Charger notre jeu
jeu = Jeu()

enFonctionnement = True

# boucle tant que running est vrai
while enFonctionnement:

    # appliquer l'arriere plan du jeu
    ecran.blit(fondEcran, (0, 0))

    # apparaitre mage
    ecran.blit(jeu.player.image, jeu.player.rect)

    #appliquer ensemble image du groupe de projectile
    jeu.player.all_projectiles.draw(ecran)

    # Verification touche + Appel fonction de deplacement
    if jeu.pressed.get(pygame.K_d):
        jeu.player.move_right()
    elif jeu.pressed.get(pygame.K_q):
        jeu.player.move_left()

    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # dès que l'évenement "fermeture" est la
        if event.type == pygame.QUIT:
            enFonctionnement = False
            pygame.quit()
        #detecter si un joueur lache une touche
        elif event.type==pygame.KEYDOWN:
            jeu.pressed[event.key] = True
            #detecte si touche e est declanché pour lancer le projectil
            if event.key==pygame.K_e:
                jeu.player.launch_Magie() #pas sure pour la majuscule


        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False