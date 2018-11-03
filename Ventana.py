# -*- coding: utf-8 -*-

import pygame,sys
from pygame.locals import *

color = (0,140,60)
colorDos = pygame.Color(255,120,9)

pygame.init()
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hola")

#background_image = load_image('C:\Users\Acer  57AV\Documents\Universidad\AYPC\Proyeco AYPC\Imagenes\planilla.jpg')

while True:
    ventana.fill(colorDos)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
#    screen.blit(background_image, (0, 0))        
    pygame.display.update()
    
def load_image(filename, transparent=False):
    image = image.convert()
    try: image = pygame.image.load(filename)   