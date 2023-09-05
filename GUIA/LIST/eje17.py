# Crea dos listas de números y encuentra los elementos que se encuentran en ambas listas.

# Crear dos listas de números
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

# Convertir las listas en conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

# Encontrar los elementos comunes
elementos_comunes = conjunto1.intersection(conjunto2)

# Convertir el resultado de nuevo a una lista
elementos_comunes_lista = list(elementos_comunes)

# Imprimir los elementos comunes
print("Elementos comunes entre las dos listas:", elementos_comunes_lista)
