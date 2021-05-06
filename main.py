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
flipped_Purple = False
jeu.player_purple.move_left(flipped_Purple)
flipped_Purple = True
flipped_Red = False

# boucle tant que running est vrai
while enFonctionnement:

    # appliquer l'arriere plan du jeu
    ecran.blit(fondEcran, (0, 0))

    # apparaitre mage
    ecran.blit(jeu.player_red.image, jeu.player_red.rect)
    ecran.blit(jeu.player_purple.image, jeu.player_purple.rect)


    # récuperer la magie du joueur

    for magie in jeu.player_red.all_projectiles:
        magie.move(flipped_Red)
    for magie in jeu.player_purple.all_projectiles:
        magie.move(flipped_Purple)

    #appliquer ensemble image du groupe de projectile
    jeu.player_red.all_projectiles.draw(ecran)
    jeu.player_purple.all_projectiles.draw(ecran)
    jeu.player_red.maj_barre_vie(ecran)
    jeu.player_purple.maj_barre_vie(ecran)

    # Verification touche + Appel fonction de deplacement
    #perso rouge
    if jeu.pressed.get(pygame.K_d):
        jeu.player_red.move_right(flipped_Red)
        flipped_Red = False
    elif jeu.pressed.get(pygame.K_q):
        jeu.player_red.move_left(flipped_Red)
        flipped_Red = True

    if jeu.player_red.jumping:
        jeu.player_red.jump_fonction()
    elif jeu.pressed.get(pygame.K_z):
        jeu.player_red.jumping=True

    #perso violet
    if jeu.pressed.get(pygame.K_RIGHT):
        jeu.player_purple.move_right(flipped_Purple)
        flipped_Purple = False
    elif jeu.pressed.get(pygame.K_LEFT):
        jeu.player_purple.move_left(flipped_Purple)
        flipped_Purple = True



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
                jeu.player_red.launch_Magie(flipped_Red)
            if event.key==pygame.K_KP0:
                jeu.player_purple.launch_Magie(flipped_Purple)

        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False