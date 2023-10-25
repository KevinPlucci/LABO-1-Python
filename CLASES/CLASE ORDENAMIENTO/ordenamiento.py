import random as rd
from time import time

ITERACIONES = 10000
lista_random_numeros = [
    rd.randint(0, 100000) for _ in range(ITERACIONES)
]

def ordenar_burbujeo(lista_numeros: list[int]):
    if not lista_numeros:
        print('La lista esta vacia')
    else:
        lista_copia = lista_numeros.copy()
        # Arranca nuestro algoritmo
        for indice_1 in range(len(lista_copia) - 1):
            for indice_2 in range(indice_1 + 1, len(lista_copia)):
                if lista_copia[indice_1] > lista_copia[indice_2]:
                    lista_copia[indice_1], lista_copia[indice_2] =\
                    lista_copia[indice_2], lista_copia[indice_1]
        return lista_copia


# el indice del elemento mas chiquito
def buscar_min(lista: list[int]):
    minimo = 0
    for indice in range(len(lista)):
        if lista[minimo] > lista[indice]:
            minimo = indice
    return minimo

def selection_sort_v1(lista: list[int]):
    if lista:
        lista_a_ordenar = lista.copy()
        lista_ordenada = []
        while len(lista_a_ordenar) > 0:
            indice_del_minimo = buscar_min(lista_a_ordenar)
            elemento_min = lista_a_ordenar.pop(indice_del_minimo)
            lista_ordenada.append(elemento_min)
        return lista_ordenada

def selection_sort_v2(lista: list[int]):
    if lista:
        lista_a_ordenar = lista.copy()
        for indice in range(len(lista_a_ordenar)):
            indice_del_minimo = buscar_min(lista_a_ordenar[indice:]) + indice
            lista_a_ordenar[indice], lista_a_ordenar[indice_del_minimo] =\
            lista_a_ordenar[indice_del_minimo], lista_a_ordenar[indice]
        return lista_a_ordenar

if __name__ == '__main__':
    start = time()
    # Ordenamiento
    lista = ordenar_burbujeo(lista_random_numeros)
    end = time()
    tiempo_total = end - start
    print(f'Burbujeo Tardo: {tiempo_total}')

    start = time()
    # Ordenamiento
    lista = selection_sort_v1(lista_random_numeros)
    end = time()
    tiempo_total = end - start
    print(f'Selection V1 Tardo: {tiempo_total}')

    start = time()
    # Ordenamiento
    lista = selection_sort_v2(lista_random_numeros)
    end = time()
    tiempo_total = end - start
    print(f'Selection V2 Tardo: {tiempo_total}')
