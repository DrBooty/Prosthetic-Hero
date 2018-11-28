# -*- coding: utf-8 -*-
import pygame
import sys
import time
 

screen_width = 800
screen_height = 600
pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))

#fondo
BLANCO = (254,254,254)
BLACK = (0,0,0)
COLOR = (150,0,0)

#Entrada Habitacion 
entradaDer = pygame.Rect(790,268,1,64)
entradaDer2 = pygame.Rect(791,268,1,64)
entradaIzq = pygame.Rect(10,268,1,64)
entradaIzq2 = pygame.Rect(10,268,1,64)
entradaUp = pygame.Rect(368,10,64,1)
entradaUp2 = pygame.Rect(368,10,64,1)
entradaDown = pygame.Rect(368,590,64,1)
entradaDown2 = pygame.Rect(368,590,64,1)

habitaciones = [
    [
#Lobby     
        pygame.Rect(0,0,800,64),
        pygame.Rect(0,64,64,536),
        pygame.Rect(736,64,64,192),
        pygame.Rect(736,340,64,202),
        pygame.Rect(64,536,736,64)
    ],
    [   
#habitacion
        pygame.Rect(0,0,365,64),
        pygame.Rect(442,0,358,64),
        pygame.Rect(0,64,64,194),
        pygame.Rect(0,340,64,258),
        pygame.Rect(64,536,301,64),
        pygame.Rect(440,536,296,64),
        pygame.Rect(736,64,64,194),
        pygame.Rect(736,340,64,258),
    
        
    ],
    [
        pygame.Rect(0,0,800,64),
        pygame.Rect(0,64,64,194),
        pygame.Rect(0,340,64,258),
        pygame.Rect(736,64,64,472),
        pygame.Rect(64,536,736,64),
    
    ],
    [
        pygame.Rect(0,0,365,64),
        pygame.Rect(440,0,360,64),
        pygame.Rect(0,64,64,536),
        pygame.Rect(736,64,64,472),
        pygame.Rect(64,536,736,64),
     
    ],
    [
        pygame.Rect(0,0,800,64),
        pygame.Rect(0,64,64,536),
        pygame.Rect(736,64,64,472),
        pygame.Rect(64,536,301,64),
        pygame.Rect(440,536,360,64),
         
     
    ]
]


entradas = [
    [
#Lobby     
        pygame.Rect(712,250,90,90)
    ],
    [   
#habitacion1
        pygame.Rect(368,10,70,90),
        pygame.Rect(712,250,90,90),
        pygame.Rect(20,250,70,90),
        pygame.Rect(368,500,70,90)
                
    ],
    [
#habitacion2
       pygame.Rect(20,250,70,90)
    
    ],
    [
#habitacion3
        pygame.Rect(368,10,70,90)
        
    ],
    [
#habitacion4        
        pygame.Rect(368,500,70,90)
     
    ]
]


#Sprites

fondo = pygame.image.load("image/biblioteca.png")
obj = pygame.Rect(300,300,32,32)
puerta = pygame.Rect(368,268,65,65)

brainLeft = pygame.image.load("image/cerebro_brazos.png")
brainRight = pygame.transform.flip(brainLeft, True, False)

#posicion inicial y velocidad
x = 368
y = 268
brainImg = brainRight
sprite1 = pygame.sprite.Sprite()
sprite1.image = brainImg
sprite1.rect = brainImg.get_rect()
    
sprite1.rect.top = y
sprite1.rect.left = x
global habNum1
habNum1 = 0


def MejoraBrazos():
    global habNum1
    entrada = 0
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pulsada = pygame.key.get_pressed()
        
        if pulsada[pygame.K_w]:
            sprite1.rect.top -= 2
            time.sleep(0.007)
            
        if pulsada[pygame.K_s]:
            sprite1.rect.top += 2
            time.sleep(0.007)
        
        if pulsada[pygame.K_a]:
            sprite1.rect.left -= 2
            sprite1.image = brainLeft
            time.sleep(0.007)

        
        if pulsada[pygame.K_d]:
            sprite1.rect.right += 2
            sprite1.image = brainRight
            time.sleep(0.007)



        for pared in habitaciones[habNum1]:
            if pared.colliderect(sprite1): 
                sprite1.rect.left = oldx                
                sprite1.rect.top = oldy
                
        
            
        if habNum1 == 0:
            
            if entradaDer.colliderect(sprite1):            
                habNum1 = 1
                sprite1.rect.top = 268
                sprite1.rect.left = 30
                
        if habNum1 == 1:
               
            if entradaIzq.colliderect(sprite1):
                habNum1 = 0
                sprite1.rect.top = 268
                sprite1.rect.left = 700
               
        if habNum1 == 1:
            
            if entradaDer2.colliderect(sprite1):
                habNum1 = 2
                sprite1.rect.top = 268
                sprite1.rect.left = 30
                
        if habNum1 == 2: 
            
            if entradaIzq2.colliderect(sprite1):
                habNum1 = 1
                sprite1.rect.top = 268
                sprite1.rect.left = 700
                
        if habNum1 == 1: 
            
            if entradaUp.colliderect(sprite1):
                habNum1 = 4
                sprite1.rect.top = 500
                sprite1.rect.left = 368
        
        if habNum1 == 4: 
            
            if entradaDown.colliderect(sprite1):
                habNum1 = 1
                sprite1.rect.top = 30
                sprite1.rect.left = 368
                
        if habNum1 == 1: 
            
            if entradaDown.colliderect(sprite1):
                habNum1 = 3
                sprite1.rect.top = 30
                sprite1.rect.left = 368
                
        if habNum1 == 3: 
            
            if entradaUp2.colliderect(sprite1):
                habNum1 = 1
                sprite1.rect.top = 500
                sprite1.rect.left = 368
            
    
                

        
        oldx = sprite1.rect.left
        oldy = sprite1.rect.top

        #Actualizamos el fondo
                
        screen.blit(fondo , (0,0))
        for pared in entradas[habNum1]:
            pygame.draw.rect(screen, BLACK, pared)   
       
            
        
    
        #se dibuja el cerebro en su ubicación actual
        screen.blit(sprite1.image, sprite1.rect)
        
        #se actualiza el render en pantalla
        pygame.display.update()
    
