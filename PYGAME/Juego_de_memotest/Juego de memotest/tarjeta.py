import pygame
from constantes import *


def crear_tarjeta(nombre_imagen: str, identificador: int, nombre_imagen_escondida: str, x: int, y: int) -> dict:
    '''
    Crea una nueva tarjeta
    Recibe como parametro el path donde estan los recursos, el nombre de la imagen y el tamaño que esta debera tener
    Retorna la tarjeta creada
    '''
    tarjeta = {}
    tarjeta["visible"] = False
    tarjeta["descubierto"] = False
    tarjeta["identificador"] = identificador
    tarjeta["superficie"] = pygame.image.load("{0}{1}".format(CARPETA_RECURSOS, nombre_imagen))
    tarjeta["superficie"] = pygame.transform.scale(tarjeta["superficie"], (ANCHO_TARJETA, ALTO_TARJETA))
    tarjeta["superficie_escondida"] = pygame.image.load("{0}{1}".format(CARPETA_RECURSOS, nombre_imagen_escondida))
    tarjeta["superficie_escondida"] = pygame.transform.scale(tarjeta["superficie_escondida"], (ANCHO_TARJETA, ALTO_TARJETA))
    tarjeta["rectangulo"] = tarjeta["superficie"].get_rect()
    tarjeta["rectangulo"].x = x
    tarjeta["rectangulo"].y = y
    return tarjeta


def obtener_cantidad_cartas(lista_tarjetas, estado):
    '''
        Me obtiene la cantidad de cartas que esten visibles y que esten o no cubiertas
        Recibe la lista de listas y un estado (True o False) si es True me devuelve las cartas descubieras sino me devuelve las cubiertas.
        Retorna dicha cantidad
    '''
    cantidad = 0
    for tarjeta in lista_tarjetas:
        if (tarjeta["descubierto"] == estado and tarjeta["visible"]):
            cantidad += 1
    return cantidad


def descubrir_tarjetas(lista_tarjetas, identificador):
    '''
        Función que se encarga de cambiarme la bandera a las tarjetas a las que el usuario haya acertado en el memotest
        recibe la lista de tarjetas y el identificador a la que le va a reemplazar la bandera descubierto
        Uso una variable contador para evitar que el bucle se ejecute completo y ahorrar recursos si ya reemplazo a dos tarjetas no tiene sentido seguir iterando
    '''
    contador = 0
    for tarjeta in lista_tarjetas:
        if tarjeta["identificador"] == identificador and tarjeta["descubierto"] == False:
            tarjeta["descubierto"] = True
            contador += 1
        elif contador == 2:
            break
            