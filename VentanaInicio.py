# -*- coding: utf-8 -*-
<<<<<<< HEAD
=======

>>>>>>> 5712e523ac874274f743c7ba416e2c16dbbfb47c
import pygame
import sys 
from Ventana import *

screen_width = 800
screen_height = 600
pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))
<<<<<<< HEAD
pygame.display.set_caption("Prostetic Hero")
fond = pygame.Rect(0,0,800,600)
Blanco = (200,200,200)

botonFigura = pygame.Rect(230,330,87,44)

titulo= pygame.image.load("image/Titulo.png")
botonn = pygame.image.load("image/Boton.png")
fondo = pygame.image.load("image/Fondo.png")


=======
fond = pygame.Rect(0,0,800,600)
Blanco = (254,254,254)


titulo= pygame.image.load("image/Titulo.png")
boton = pygame.image.load("image/Boton.png")
>>>>>>> 5712e523ac874274f743c7ba416e2c16dbbfb47c

def PantallaInicio():
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
<<<<<<< HEAD
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = event.pos
            if botonFigura.colliderect([mouse[0], mouse[1], 1, 1]):
                game_loop()
                
            
               
            
        screen.blit(fondo, (0,0))        
        screen.blit(titulo, (210,230)) 
        screen.blit(botonn, (230,330))
=======
        
        pygame.draw.rect(screen, Blanco, fond)        
        screen.blit(titulo, (210,230)) 
        #screen.blit(boton, (230,330))
>>>>>>> 5712e523ac874274f743c7ba416e2c16dbbfb47c
        
        pygame.display.update()
                
PantallaInicio()