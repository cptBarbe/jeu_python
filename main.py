import pygame
from pygame.locals import *

pygame.init()

# def musique(mus):

def pause():
    for event in pygame.event.get():
        fond = pygame.image.load("fond.jpg")
        fenetre.blit(fond, (0, 0))
        pygame.display.flip()

        if event.key == K_ESCAPE:
            return 0

"""
def alterner(a, l, r):
    if a % 2 == 1:
        a = a + 1
        perso = pygame.image.load(l).convert_alpha()
        print "Gauche"

    else:
        a = a + 1
        perso = pygame.image.load(r).convert_alpha()
        print "Droite"
"""
# def pnj():

# variables du jeu
fenetre = pygame.display.set_mode((800, 540))
continuer = True
fond = pygame.image.load("terrain2.png").convert()
perso = pygame.image.load("face.png").convert_alpha()
perso_position = perso.get_rect()
start_fond = pygame.image.load("fond.jpg")
start_boutton = pygame.image.load("start.png")
menu = True
jeu = True
a = 1

# "blittage" des surfaces
fenetre.blit(start_fond, (0,0))
fenetre.blit(start_boutton, (270,400))
pygame.display.flip() # raffriachissement des surfaces

while continuer: # boucle principale (strucutre du jeu)
#    pygame.time.Clock().tick(100)
    pygame.key.set_repeat(10, 60)

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        else:
            while menu: # boucle du menu
#                print "Menu"
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        menu = 0

            while jeu: # boucle du jeu
#                print "Jeu"
                for event in pygame.event.get():
                    if event.type == QUIT:
                        print "fin du jeu"
                        continuer = False
                        
                    if event.type == KEYDOWN:
                        print perso_position
                        
                        if event.key == K_a:
                            perso_position = perso_position.move(0, 5)
                            #alterner(1, "faceL.png", "faceR.png")
                            if a % 2 == 1:
                                a = a + 1
                                perso = pygame.image.load("faceL.png").convert_alpha()
                                
                            else:
                                a = a + 1
                                perso = pygame.image.load("faceR.png").convert_alpha()

                        if event.key == K_u:
                            perso_position = perso_position.move(5, 0)
                            #alterner(1, "r1.png", "r2.png")
                            if a % 2 == 1:
                                a = a + 1
                                perso = pygame.image.load("r1.png").convert_alpha()
                            else:
                                a = a + 1
                                perso = pygame.image.load("r2.png").convert_alpha()
                                        
                        if event.key == K_o:
                            perso_position = perso_position.move(-5, 0)
                            #alterner(1,"l1.png", "l2.png")

                            if a % 2 == 1:
                                a = a + 1
                                perso = pygame.image.load("l1.png").convert_alpha()
                                    
                            else:
                                a = a + 1
                                perso = pygame.image.load("l2.png").convert_alpha()
                            
                        if event.key == K_QUOTE:
                            perso_position = perso_position.move(0, -5)
                            #alterner(1,"haut1.png", "haut2.png")

                            if a % 2 == 1:
                                a = a + 1
                                perso = pygame.image.load("haut1.png").convert_alpha()

                            else:
                                a = a + 1
                                perso = pygame.image.load("haut2.png").convert_alpha()
                                        
                        if event.key == K_ESCAPE:
                            jeu = False
                            print jeu
                            pause()

                continuer = True
                fenetre.blit(fond, (0,0))
                fenetre.blit(perso, perso_position)
                pygame.display.flip()

pygame.quit()
