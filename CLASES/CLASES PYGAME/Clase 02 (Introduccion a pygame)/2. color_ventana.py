import pygame

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

pygame.init()

ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Prueba eventos")
ventana_ppal.fill(ROJO)#Metodo fill llena con un color la superficie de la ventana
flag_run = True

while flag_run:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False
            
    
    #Este metodo siempre tiene que estar, ya que es el encargado de actualizar todo lo que suceda dentro de la ventana
    pygame.display.update()

pygame.quit()