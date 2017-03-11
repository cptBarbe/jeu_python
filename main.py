import pygame
import random

from pygame.locals import *
from random import *


pygame.init()

# def musique(musique):


# def pnj():


def pause():
    pause = True

    while pause:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause = False

            if event.type == QUIT:
                exit()
                    
        fond = pygame.image.load("fond.jpg")
        fenetre.blit(fond, (0, 0))
        pygame.display.flip()

            
def altern(a, l, r):
    if a % 2 == 1:
        a = a + 1
        perso = pygame.image.load(l).convert_alpha()
        # print "Gauche"

    else:
        a = a + 1
        perso = pygame.image.load(r).convert_alpha()
        # print "Droite"

    return perso


# variables du jeu
imagePATH = "/home/joseph/Bureau/jeu_python/tiles"
musiquePATH = "/home/joseph/Bureau/jeu_python/musique"
fenetre = pygame.display.set_mode((800, 540)) # 50 * 33
fond = pygame.image.load("terrain2.png").convert()
perso = pygame.image.load("face.png").convert_alpha()
perso_position = perso.get_rect()
start_fond = pygame.image.load("fond.jpg")
start_boutton = pygame.image.load("start.png")

continuer = True
menu = True
jeu = True

a = 1

pygame.key.set_repeat(1, 50)

while continuer: # boucle principale (strucutre du jeu)

    for event in pygame.event.get():

        if event.type == QUIT:
            exit()
                        
        if event.type == KEYDOWN:
            print perso_position           

            if event.key == K_a:
                perso_position = perso_position.move(0, 5)
                # altern(1, "faceL.png", "faceR.png")

                if a % 2 == 1:
                    a = a + 1
                    perso = pygame.image.load("faceL.png").convert_alpha()
                                
                else:
                    a = a + 1
                    perso = pygame.image.load("faceR.png").convert_alpha()

            if event.key == K_u:
                perso_position = perso_position.move(5, 0)
                # altern(1, "r1.png", "r2.png")
                if a % 2 == 1:
                    a = a + 1
                    perso = pygame.image.load("r1.png").convert_alpha()

                else:
                    a = a + 1
                    perso = pygame.image.load("r2.png").convert_alpha()
                                        
            if event.key == K_o:
                perso_position = perso_position.move(-5, 0)
                # altern(1,"l1.png", "l2.png")

                if a % 2 == 1:
                    a = a + 1
                    perso = pygame.image.load("l1.png").convert_alpha()
                                    
                else:
                    a = a + 1
                    perso = pygame.image.load("l2.png").convert_alpha()
                            
            if event.key == K_QUOTE:
                perso_position = perso_position.move(0, -5)
                # altern(1,"haut1.png", "haut2.png")

                if a % 2 == 1:
                    a = a + 1
                    perso = pygame.image.load("haut1.png").convert_alpha()
                    
                else:
                    a = a + 1
                    perso = pygame.image.load("haut2.png").convert_alpha()
                                        
            if event.key == K_ESCAPE:
                #jeu = False
                pause()

    continuer = True
    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, perso_position)
    pygame.display.flip()

pygame.quit()