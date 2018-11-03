# -*- coding: utf-8 -*-
import pygame,sys
from pygame.locals import *



pygame.init()
ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("Hola")

Mi_imagen = pygame.image.load("image/tontoarturo.png")
posx= 0
posy = 0
velocidad = 2
Blanco = (255,255,255)
derecha = True


while True:
    ventana.fill(Blanco)
    ventana.blit(Mi_imagen,(posx,posy))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
