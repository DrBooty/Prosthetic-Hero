import pygame
import sys

#config
screen_width = 800
screen_height = 600
pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))

#fondo
BLANCO = (254,254,254)
BLACK = (0,0,0)
#habitacion = pygame.image.load("image/habitacion1.jpg")

habitaciones = [
    [
        pygame.Rect(0,0,800,64),
        pygame.Rect(0,64,64,536),
        pygame.Rect(736,64,64,202),
        pygame.Rect(736,334,64,202),
        pygame.Rect(64,536,736,64)
    ]
]

#Sprites


brainLeft = pygame.image.load("image/cerebro.png")
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

habitacion1Pos = [0,0]

def game_loop():
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pulsada = pygame.key.get_pressed()
        
        if pulsada[pygame.K_w]:
            sprite1.rect.top -= 1
            
        if pulsada[pygame.K_s]:
            sprite1.rect.top += 1
        
        if pulsada[pygame.K_a]:
            sprite1.rect.left -= 1
            sprite1.image = brainLeft

        
        if pulsada[pygame.K_d]:
            sprite1.rect.right += 1
            sprite1.image = brainRight



        for pared in habitaciones[0]:
            if pared.colliderect(sprite1): 
                sprite1.rect.left = oldx                
                sprite1.rect.top = oldy

        
        oldx = sprite1.rect.left
        oldy = sprite1.rect.top

        #Actualizamos el fondo
        
        #screen.blit(habitacion, habitacion1Pos) 
        pygame.draw.rect(screen,BLACK,(0,0,800,600))

        for pared in habitaciones[0]:
            pygame.draw.rect(screen, BLANCO, pared)

        
       
        #se dibuja el cerebro en su ubicación actual
        screen.blit(sprite1.image, sprite1.rect)
        
        #se actualiza el render en pantalla
        pygame.display.update() 

game_loop()