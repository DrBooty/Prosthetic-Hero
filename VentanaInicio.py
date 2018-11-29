# -*- coding: utf-8 -*-
import pygame
import sys 
from Ventana import *

screen_width = 800
screen_height = 600
pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Prostetic Hero")
fond = pygame.Rect(0,0,800,600)
Blanco = (200,200,200)

botonFigura = pygame.Rect(230,330,87,44)

titulo= pygame.image.load("image/Titulo.png")
botonn = pygame.image.load("image/Boton.png")
fondo = pygame.image.load("image/Fondo.png")



def PantallaInicio():
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = event.pos
            if botonFigura.colliderect([mouse[0], mouse[1], 1, 1]):
                game_loop()
                
            
               
            
        screen.blit(fondo, (0,0))        
        screen.blit(titulo, (210,230)) 
        screen.blit(botonn, (230,330))
        
        pygame.display.update()
                
PantallaInicio()