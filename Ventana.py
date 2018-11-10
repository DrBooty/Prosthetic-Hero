import pygame
import sys


#config
screen_width = 600
screen_height = 300
pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))

#fondo
BLANCO = (254,254,254)
habitacion = pygame.image.load("image/habitacion1.jpg")

#Sprites
brainLeft = pygame.image.load("image/cerebro.png")
brainRight = pygame.transform.flip(brainLeft, True, False)

#posicion inicial y velocidad
brainPosition = [35,35]
speed = 0.5
habitacion1Pos = [0,0]
#funcion que garantiza que la accion se realizara en todo momento
def game_loop():
    
    #inicializamos el sprite
    brainImg = brainRight
    
    #ejecutamos el ciclo que recibira los eventos
    while True:
        
        #capturamos si el evento es de salida
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #si no hay eventos de salida capturamos todas las teclas presionadas
        keys = pygame.key.get_pressed()

        #dependiendo de la tecla presionada, se actualizarán las coordenadas de ubicacion del cerebro
        #tambien se limita el espacio en que el sprite puede moverse
        if keys[pygame.K_w]:
            if brainPosition[1] > 0:
                brainPosition[1] -= speed
            
        if keys[pygame.K_s]:
            if brainPosition[1] < 536:
                brainPosition[1] += speed
        
        #en ocasiones especiales se requerira cambiar la orientacion del sprite
        if keys[pygame.K_a]:
            if brainPosition[0] > 0:
                brainPosition[0] -= speed
                brainImg = brainLeft
        
        if keys[pygame.K_d]:
            if brainPosition[0] < 736:
                brainPosition[0] += speed
                brainImg = brainRight


        #Actualizamos el fondo
        screen.blit(habitacion, habitacion1Pos) 
        
        #se dibuja el cerebro en su ubicación actual
        screen.blit(brainImg, brainPosition) 

        #se actualiza el render en pantalla
        pygame.display.update() 

game_loop()