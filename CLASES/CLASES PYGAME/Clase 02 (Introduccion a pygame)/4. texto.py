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
icono = pygame.image.load("utn_icono.jpg")
pygame.display.set_icon(icono)

#Creamos una fuente con tipografía y tamaño
fuente = pygame.font.SysFont("consolas",60)

#El metodo render de la fuente lo que hace es crear una superficie con el texto que pasamos como parametro.
#fuente.render(string, antialias:como renderiza, color_texto, color_fondo)
texto = fuente.render("Bienvenidos a Laboratorio I", False, ROJO, AZUL_CLARO)

ventana_ppal.fill(VERDE)
flag_run = True

while flag_run:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False
    
    #BLIT imprime en la ventana principal una superficie. En este caso nuestra superficie es el texto.
    ventana_ppal.blit(texto,(50,50))#En la posicion (X,Y) de la ventana   
    pygame.display.update()

pygame.quit()