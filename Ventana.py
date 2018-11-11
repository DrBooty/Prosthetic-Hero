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

#Sprites
paredUp = pygame.Rect(0,0,800,64)
paredLeft = pygame.Rect(0,64,64,536)
paredRight = pygame.Rect(736,64,64,536)
paredDown = pygame.Rect(64,536,736,64)

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
            sprite1.rect.top -= 0.5
        if pulsada[pygame.K_s]:
            sprite1.rect.top += 1/2
        if pulsada[pygame.K_a]:
            sprite1.rect.left -= 0.5
        if pulsada[pygame.K_d]:
            sprite1.rect.left += 1/2
        '''
        if pulsada[pygame.K_w]:
            sprite1.rect.top -= 0.5
            
        if pulsada[pygame.K_s]:
            sprite1.rect.top += 0.5
            print ("mover abajo")
            
        if pulsada[pygame.K_a]:
            sprite1.rect.left -= 0.5
            
        if pulsada[pygame.K_d]:
            sprite1.rect.left += 0.5
            print ("mover derecha")
          '''  
        if paredUp.colliderect(sprite1): 
            sprite1.rect.top = oldy
            
        if paredDown.colliderect(sprite1):
            sprite1.rect.top = oldy
        
        if paredLeft.colliderect(sprite1):
            sprite1.rect.left = oldx
            
        if paredRight.colliderect(sprite1):
            sprite1.rect.left = oldx
        
        oldx = sprite1.rect.left
        oldy = sprite1.rect.top

        
      

     
                
      
        
        
        


        #Actualizamos el fondo
        
        #screen.blit(habitacion, habitacion1Pos) 
        pygame.draw.rect(screen,BLACK,(0,0,800,600))
        pygame.draw.rect(screen, BLANCO,paredUp)
        pygame.draw.rect(screen, BLANCO,paredLeft)
        pygame.draw.rect(screen, BLANCO,paredRight)
        pygame.draw.rect(screen, BLANCO,paredDown)
        
       
        #se dibuja el cerebro en su ubicación actual
        screen.blit(sprite1.image, sprite1.rect)
        

        #se actualiza el render en pantalla
        pygame.display.update() 

game_loop()