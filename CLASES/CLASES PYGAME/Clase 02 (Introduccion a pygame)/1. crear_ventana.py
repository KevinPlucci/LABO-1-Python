import pygame, sys
from pygame.locals import *

pygame.init()#Para inicializar pygame

pygame.display.set_mode((500,200)) # en pixeles (width=Largo, height=Alto)
pygame.display.set_caption("Mi primer ventana.")#Titulo de la ventana

flag_run = True
while flag_run:#Bucle infinito. Todo lo que necesitamos que se repita de manera indeterminada...
    #Las siguientes lineas permiten capturar eventos. Por ejemplo si el usuario presiona alguna tecla especifica.
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:#Preguntamos si presionó X. (Esto es el evento QUIT de pygame)
            flag_run = False
    
pygame.quit()