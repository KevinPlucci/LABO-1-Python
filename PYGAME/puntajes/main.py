import pygame
from data_puntajes import lista_puntajes
from utils import *

# Definimos tamaño de la ventana en pixeles
ANCHO_VENTANA = 800
ALTO_VENTANA = 600

# Inicializamos pygame
pygame.init()

# Creamos la ventana del juego
ventana_juego = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

# Flag que controla la ejecución del juego
juego_on = True

# Cargamos la imagen del fondo
img_fondo = pygame.image.load(r"recursos\img\fondo.png")

# Cargamos la imagen de la tabla
img_tabla_puntajes = pygame.image.load(r"recursos\img\tabla_puntajes.png")
pos_img_tabla_puntajes = ((ANCHO_VENTANA - img_tabla_puntajes.get_width()) // 2, 10)

# Creamos el texto del titulo
font_titulo = pygame.font.Font(r"recursos\fonts\Halimount.otf", 50)
txt_titulo = font_titulo.render("Puntajes", True, "white")
pos_txt_titulo = ((ANCHO_VENTANA - txt_titulo.get_width()) // 2, 35)

# Creamos el texto del boton
font_boton = pygame.font.Font(r"recursos\fonts\Halimount.otf", 30)
txt_boton = font_boton.render("Jugar de nuevo", True, "white")
pos_txt_boton = ((ANCHO_VENTANA - txt_titulo.get_width()) // 2, 515)

# Creamos el texto de la tabla
font_tabla = pygame.font.Font(r"recursos\fonts\Halimount.otf", 35)
lista_puntaje_txt = []

y = 135

for item in lista_puntajes:
    # Si estamos en la primera vuelta, utilizamos la tipografia color blanco
    if len(lista_puntaje_txt) == 0:
        color_txt = (255, 255, 255)
    else:
        color_txt = (109, 30, 3)

    nro_txt = font_tabla.render(str(item["nro"]), True, (255, 76, 114))
    nombre_txt = font_tabla.render(
        formatear_nombre_jugador(str(item["nombre"])), True, color_txt
    )
    puntaje_txt = font_tabla.render(
        formatear_puntaje(str(item["puntaje"])), True, color_txt
    )

    lista_puntaje_txt.append((nro_txt, (260, y)))
    lista_puntaje_txt.append((nombre_txt, (300, y)))
    lista_puntaje_txt.append((puntaje_txt, (460, y)))

    y += 50

while juego_on:
    # Nos quedamos con los eventos
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        # En el caso que se ocurra el evento de salir, finalizamos el bucle principal
        if evento.type == pygame.QUIT:
            juego_on = False

    # Dibujamos los elementos
    ventana_juego.blit(img_fondo, (0, 0))
    ventana_juego.blit(img_tabla_puntajes, pos_img_tabla_puntajes)
    ventana_juego.blit(txt_titulo, pos_txt_titulo)
    ventana_juego.blits(lista_puntaje_txt)
    ventana_juego.blit(txt_boton, pos_txt_boton)

    # Mostramos los cambios
    pygame.display.flip()

pygame.quit()
