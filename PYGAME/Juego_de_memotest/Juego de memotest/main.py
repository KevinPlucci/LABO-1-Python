import pygame
from constantes import *

import tablero
import tarjeta
import utils


def terminar_juego(pantalla, mensaje, color):
    '''
    Función que se encarga de mostrar una imagen con el juego terminado al usuario
    recibe la pantalla, un mensaje y el color de ese mismo
    '''
    if mensaje != False:
        texto = utils.generar_texto("Arial", 50, mensaje, color)
        texto_salir = utils.generar_texto(
            "Arial", 20, "Presione el boton espacio para salir", color)
        esta_corriendo = True
        while (esta_corriendo):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esta_corriendo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        esta_corriendo = False

            pantalla_juego.fill(COLOR_NEGRO)
            imprimir_superficie(
                pantalla, texto,  ANCHO_PANTALLA // 10, ALTO_PANTALLA / 2)
            imprimir_superficie(pantalla, texto_salir,
                                ANCHO_PANTALLA/2, ALTO_PANTALLA-20)
            pygame.display.flip()

        pygame.quit()


def imprimir_superficie(pantalla, superficie, x, y):
    '''
    Función que se encarga de imprimir una superficie que le paso
    Recibe la pantalla, la superficie para imprimir, una posición X y posición Y
    '''
    pantalla.blit(superficie, (x, y))


def terminar_partida(cronometro, cantidad_movimientos, tablero):
    '''
    Verifico si el usuario ganó o perdio la partida
    si se queda sin movimientos o sin tiempo perdió 
    si todos las tarjetas del tablero están descubiertas el jugador gano
    Recibe el cronometro, los movimientos actuales del jugador y el tablero
    Si el jugador gano cambia la pantalla y muestra (VICTORIA O DERROTA DEPENDIENDO DE LO QUE HAYA PASADO)
    Retorna True si la partida termino y False si no lo terminó.
    '''
    retorno = False
    if cantidad_movimientos == 0 or cronometro == 0:
        retorno = True
    elif tarjeta.obtener_cantidad_cartas(tablero["tarjetas"], True) == CANTIDAD_TARJETAS:
        retorno = True

    return retorno

# Configuración inicial de pygame
pygame.init()
pantalla_juego = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption('Los Simpsons Memotest')
clock_fps = pygame.time.Clock() # Creamos un Clock para poder fijar los FPS


# Creamos eventos de tiempo
evento_1000ms = pygame.USEREVENT
pygame.time.set_timer(evento_1000ms, 1000)

# Configuracion inicial del juego
tablero_juego = tablero.crear_tablero()
cronometro = TIEMPO_JUEGO
cantidad_movimientos = CANTIDAD_MOVIMIENTOS
cantidad_tarjetas_cubiertas = CANTIDAD_TARJETAS_UNICAS * 2
cantidad_tarjetas_descubiertas = 0


esta_corriendo = True

while esta_corriendo:
    tiempo = clock_fps.tick(FPS)
    
    texto_cronometro = utils.generar_texto(
        "Arial", TAMANIO_TEXTO, "Tiempo:{0}".format(cronometro), COLOR_NEGRO)
    texto_movimientos = utils.generar_texto(
        "Arial", TAMANIO_TEXTO, "Movimientos Restantes:{0}".format(cantidad_movimientos), COLOR_NEGRO)
    texto_puntuación = utils.generar_texto("Arial", TAMANIO_TEXTO, "{0}/{1} Tarjetas".format(
        cantidad_tarjetas_descubiertas, cantidad_tarjetas_cubiertas), COLOR_NEGRO)

    if terminar_partida(cronometro, cantidad_movimientos, tablero_juego):
        esta_corriendo = False
        color = COLOR_VERDE
        mensaje = "Felicidades usted ha ganado"
        if cronometro == 0 or cantidad_movimientos == 0:
            color = COLOR_ROJO
            mensaje = "Game Over usted ha perdido "
        terminar_juego(pantalla_juego, mensaje, color)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            esta_corriendo = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            SONIDO_CLICK.play()
            if tablero.detectar_colision(tablero_juego, pos) != None:
                SONIDO_VOLTEAR.play()
                if tarjeta.obtener_cantidad_cartas(tablero_juego["tarjetas"], False) == 1:
                    cantidad_movimientos -= 1
        if event.type == evento_1000ms:
            cronometro -= 1

    cantidad_tarjetas_descubiertas = tarjeta.obtener_cantidad_cartas(
        tablero_juego["tarjetas"], True)
    tablero.actualizar_tablero(tablero_juego)
    pantalla_juego.fill(COLOR_BLANCO)
    tablero.dibujar_tablero(tablero_juego, pantalla_juego)
    imprimir_superficie(pantalla_juego, texto_cronometro,
                        0, ALTO_PANTALLA-TAMANIO_TEXTO)
    imprimir_superficie(pantalla_juego, texto_puntuación,
                        0, ALTO_PANTALLA-TAMANIO_TEXTO * 2)
    imprimir_superficie(pantalla_juego, texto_movimientos,
                        0, ALTO_PANTALLA-TAMANIO_TEXTO * 3)
    pygame.display.flip()

pygame.quit()
