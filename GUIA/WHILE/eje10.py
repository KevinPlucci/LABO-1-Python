# Dada una lista de números, imprimir la cantidad de números pares en la lista.

# Definir una lista de números
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Inicializar una variable para contar los números pares
cantidad_pares = 0

# Inicializar un índice para recorrer la lista
indice = 0

# Usar un bucle while para recorrer la lista
while indice < len(lista_numeros):
    # Obtener el número en la posición actual
    numero = lista_numeros[indice]

    # Verificar si el número es par
    if numero % 2 == 0:
        cantidad_pares += 1

    # Incrementar el índice para avanzar en la lista
    indice += 1

# Imprimir la cantidad de números pares
print("La cantidad de números pares en la lista es:", cantidad_pares)
