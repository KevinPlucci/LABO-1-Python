import pygame
import time
import random
import tarjeta
from constantes import *

def crear_tablero():
    '''
    Crea una lista de tarjetas
    Retorna un dict tablero
    '''
    tablero = {}
    # TODO ESTO CON PASS
    tablero["tarjetas"] = generar_lista_tarjetas()
    tablero["tiempo_ultimo_destape"] = 0
    tablero["primer_tarjeta_seleccionada"] = None
    tablero["segunda_tarjeta_seleccionada"] = None
    return tablero

def generar_lista_tarjetas()->list:
    '''
    Función que se encarga de generar una lista de tarjetas ordenada aleatoriamente
    El for x me recorre todas las posiciones de x usando de step el ancho de la tarjeta
    El for y me recorre todas las posiciones de x usando de step el alto de la tarjeta
    Por ende me va a generar la cantidad de tarjetas que le especifique anteriormente 
    ajustandose a la resolución de mi pantalla de manera dinámica
    Usa la función random.shuffle para generar de manera aleatoria los identificadores. Genera una lista de identificadores
    en donde se repiten dos veces el mismo ya que en un memotest se repiten dos veces la misma carta
    Retorna la lista de las tarjetas generadas
    '''
    lista_tarjetas = []
    indice = 0
    lista_id = generar_lista_ids_tarjetas() 
    print(lista_id)

    for x in range(0, CANTIDAD_TARJETAS_H * ANCHO_TARJETA, ANCHO_TARJETA):
        for y in range(0, CANTIDAD_TARJETAS_V * ALTO_TARJETA, ALTO_TARJETA):
            # TODO ESTO CON PASS
            tarjeta_creada = tarjeta.crear_tarjeta("0{0}.png".format(lista_id[indice]),lista_id[indice],r"00.png",x,y)
            lista_tarjetas.append(tarjeta_creada)
            indice += 1
    
    return lista_tarjetas

def generar_lista_ids_tarjetas():
    lista_id = list(range(1,CANTIDAD_TARJETAS_UNICAS+1)) #Creo una lista con todos los identificadores posibles
    lista_id.extend(list(range(1,CANTIDAD_TARJETAS_UNICAS+1))) #Extiendo esa lista con otra lista identica ya que hay dos tarjetas iguales en cada tablero (mismo identificador)
    random.seed(time.time())
    random.shuffle(lista_id) #Esos identificadores los desordeno de forma al azar
    return lista_id
    

def detectar_colision(tablero,pos_xy):
    '''
    verifica si existe una colision alguna tarjetas del tablero y la coordenada recibida como parametro
    Recibe como parametro el tablero y una tupla (X,Y)
    Retorna el identificador de la tarjeta que colisiono con el mouse y sino retorna None
    '''
    retorno = None
    print(pos_xy)
    lista_tarjetas = tablero["tarjetas"]
    print(tarjeta.obtener_cantidad_cartas(lista_tarjetas, False))
    if(tarjeta.obtener_cantidad_cartas(lista_tarjetas, False) < 2):#Si hay al menos de 2 tarjetas descubiertas
        for aux_tarjeta in lista_tarjetas:
            if(aux_tarjeta["rectangulo"].collidepoint(pos_xy) and not aux_tarjeta["visible"]):
                if tablero["primer_tarjeta_seleccionada"] == None:
                    tablero["primer_tarjeta_seleccionada"] = aux_tarjeta
                elif tablero["segunda_tarjeta_seleccionada"] == None:
                    tablero["segunda_tarjeta_seleccionada"] = aux_tarjeta
                aux_tarjeta["visible"]=True
                print("Se colisiono con la tarjeta de id {0}".format(aux_tarjeta["identificador"]))
                tablero["tiempo_ultimo_destape"] = pygame.time.get_ticks()#Especifico el tiempo en el que se hizo click
                retorno = aux_tarjeta["identificador"]
    return retorno

def actualizar_tablero(tablero):
    '''
    Verifica si es necesario actualizar el estado de alguna tarjeta, en funcion de su propio estado y el de las otras
    Recibe como parametro el tablero
    '''
    tiempo_actual = pygame.time.get_ticks()
    if(tiempo_actual - tablero["tiempo_ultimo_destape"] > TIEMPO_MOVIMIENTO and tablero["tiempo_ultimo_destape"] > 0):#Si el tiempo en el que hizo click o tuvo un fallo supera los tres segundos puedo volver a clickear
        tablero["tiempo_ultimo_destape"] = 0
        lista_tarjetas = tablero["tarjetas"]
        for aux_tarjeta in lista_tarjetas:
            if(aux_tarjeta["descubierto"]==False):
                aux_tarjeta["visible"]=False
                tablero["primer_tarjeta_seleccionada"] = None
                tablero["segunda_tarjeta_seleccionada"] = None
    if(tablero["tiempo_ultimo_destape"] > 0):
        retorno = encontrar_tarjetas(tablero)
        if retorno != None:
            if retorno:
                tablero["tiempo_ultimo_destape"] = 0
                print("Coinciden las imagenes")
                SONIDO_ACIERTO.play()
            else:
                SONIDO_ERROR.play()
                tablero["tiempo_ultimo_destape"] -= 2000
                if tablero["tiempo_ultimo_destape"] < 0:
                    tablero["tiempo_ultimo_destape"] = 500

                print("No coinciden las imagenes")

            tablero["primer_tarjeta_seleccionada"] = None
            tablero["segunda_tarjeta_seleccionada"] = None

def encontrar_tarjetas(tablero):
    '''
    Funcion que se encarga de encontrar un match en la selección de las tarjetas del usuario.
    Si el usuario selecciono dos tarjetas está función se encargara de verificar si el identificador 
    de las mismas corresponde si es así retorna True, sino False. 
    En caso de que no hayan dos tarjetas seleccionadas retorna None
    '''
    retorno = None
    if tablero["primer_tarjeta_seleccionada"] != None and tablero["segunda_tarjeta_seleccionada"] != None:
        retorno = False
        if tablero["primer_tarjeta_seleccionada"]["identificador"] == tablero["segunda_tarjeta_seleccionada"]["identificador"]:
            tarjeta.descubrir_tarjetas(tablero["tarjetas"], tablero["primer_tarjeta_seleccionada"]["identificador"])
            retorno = True

    return retorno

def dibujar_tablero(tablero,pantalla_juego):
    '''
    Dibuja todos los elementos del tablero en la superficie recibida como parametro
    Recibe como parametro el tablero
    '''
    lista_tarjetas = tablero["tarjetas"]
    for tarjeta_aux in lista_tarjetas:
        if(tarjeta_aux["visible"]):
            pantalla_juego.blit(tarjeta_aux["superficie"],tarjeta_aux["rectangulo"])
        else:
            pantalla_juego.blit(tarjeta_aux["superficie_escondida"],tarjeta_aux["rectangulo"])
     