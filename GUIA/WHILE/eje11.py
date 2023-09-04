# Dada una lista de palabras, imprimir todas las palabras que tengan una longitud mayor a 5 caracteres.

# Definir una lista de palabras
lista_de_palabras = ["manzana", "banana", "naranja", "uva", "sandía", "pera", "kiwi"]

# Inicializar un índice
indice = 0

# Usar un bucle while para imprimir palabras con longitud mayor a 5 caracteres
while indice < len(lista_de_palabras):
    palabra = lista_de_palabras[indice]
    if len(palabra) > 5:
        print(palabra)
    indice += 1
