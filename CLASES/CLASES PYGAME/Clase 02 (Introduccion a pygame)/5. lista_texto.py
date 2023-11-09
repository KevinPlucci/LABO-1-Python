import pygame

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AZUL_CLARO = (0,150,255)

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

lista_nombres = ["Mariano", "Giovanni", "Marcos", "Lucas", "German"]

pygame.init()

ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("UTN COCOS CAPITAL")
icono = pygame.image.load("Clase 02 (Introduccion a pygame)\\utn_icono.jpg")
pygame.display.set_icon(icono)

#Creamos una fuente con tipografía y tamaño
fuente = pygame.font.SysFont("arial", 30)
texto = fuente.render("1. El tipo de instrumento mas comprado es: CEDEAR", True, ROJO, AZUL_CLARO)
ventana_ppal.blit(texto,(50,50))
texto = fuente.render("2. El promedio de dinero invertido es: $50352.33", True, ROJO, AZUL_CLARO)
ventana_ppal.blit(texto,(50,100))   
texto = fuente.render("3. El porcentaje de BONOS comprados es: 26%", True, ROJO, AZUL_CLARO)
ventana_ppal.blit(texto,(50,150))    
#El metodo render de la fuente lo que hace es crear una superficie con el texto que pasamos como parametro.

flag_run = True

y = 50
while flag_run:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False
    # for nombre in lista_nombres:
    #     texto = fuente.render(nombre, True, ROJO, AZUL_CLARO)
    #     y += 40 
    #     ventana_ppal.blit(texto,(50,y))#En la posicion (X,Y) de la ventana   
    pygame.display.update()

pygame.quit()