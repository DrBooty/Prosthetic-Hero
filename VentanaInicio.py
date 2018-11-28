# -*- coding: utf-8 -*-

import pygame
import sys 
from Ventana import *

screen_width = 800
screen_height = 600
pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))
fond = pygame.Rect(0,0,800,600)
Blanco = (254,254,254)


titulo= pygame.image.load("image/Titulo.png")
boton = pygame.image.load("image/Boton.png")

def PantallaInicio():
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.draw.rect(screen, Blanco, fond)        
        screen.blit(titulo, (210,230)) 
        #screen.blit(boton, (230,330))
        
        pygame.display.update()
                
PantallaInicio()