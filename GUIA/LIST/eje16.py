""" Crea dos listas con la misma cantidad de elementos y luego crea una tercera lista que contenga los elementos de ambas listas intercalados. 
Por ejemplo, si las dos listas son [1, 2, 3] y ["a", "b", "c"], la tercera lista debería ser [1, "a", 2, "b", 3, "c"].
"""
# Crear dos listas con la misma cantidad de elementos
lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]

# Crear una tercera lista con elementos intercalados
lista_intercalada = []

# Iterar a través de ambas listas e intercalar elementos
for i in range(len(lista1)):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

# Imprimir la lista intercalada
print("La lista intercalada es:", lista_intercalada)
