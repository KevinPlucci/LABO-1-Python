# Crear una función que cuente la cantidad de veces que aparece un elemento en una lista. Recibe una lista y un elemento como parámetros y devuelve la cantidad de veces que aparece en la lista.


def contar_elemento_en_lista(lista, elemento):
    contador = 0
    for item in lista:
        if item == elemento:
            contador += 1
    return contador


# Ejemplo de uso
mi_lista = [1, 2, 2, 3, 4, 2, 5]
elemento_a_contar = 2
cantidad = contar_elemento_en_lista(mi_lista, elemento_a_contar)
print(f"{elemento_a_contar} aparece {cantidad} veces en la lista.")
