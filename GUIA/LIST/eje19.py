"""Crea una lista vacía y pide al usuario que ingrese una palabra. 
Luego, agrega la palabra a la lista si no se encuentra ya en la lista. 
Repite este proceso hasta que la lista tenga al menos 5 palabras.
"""

# Crear una lista vacía para almacenar las palabras
lista_palabras = []

# Solicitar al usuario que ingrese palabras hasta que haya al menos 5
while len(lista_palabras) < 5:
    palabra = input("Ingrese una palabra: ")

    # Verificar si la palabra ya está en la lista
    if palabra not in lista_palabras:
        lista_palabras.append(palabra)
    else:
        print("La palabra ya está en la lista. Intente nuevamente.")

# Imprimir la lista de palabras
print("Lista de palabras ingresadas:")
for palabra in lista_palabras:
    print(palabra)
