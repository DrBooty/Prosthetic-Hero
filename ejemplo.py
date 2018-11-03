# -*- coding: utf-8 -*-
import pygame,sys
from pygame.locals import *
#from ramdom import randint
 
pygame.init()
ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("Valentina es fea")

Mi_imagen = pygame.image.load("image/tontoarturo.png")
posx= 0
posy = 0
velocidad = 6
Blanco = (150,150,150)
derecha = True

while True :
    ventana.fill(Blanco)
    ventana.blit(Mi_imagen,(posx,posy))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type== pygame.KEYDOWN:
            if event.key == K_LEFT:
                posx-=velocidad
            elif event.key == K_RIGHT:
                posx+=velocidad
            elif event.key == K_UP:
                posy-=velocidad
            elif event.key == K_DOWN:
                posy+= velocidad
    pygame.display.update()