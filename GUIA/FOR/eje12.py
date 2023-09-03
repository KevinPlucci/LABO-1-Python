# Dada una lista de números, imprimir la cantidad de números pares en la lista.

# Lista de números
numeros = [5, 10, 7, 2, 8, 15, 3, 12]

# Inicializar la cantidad de números pares
cantidad_pares = 0

# Iterar a través de la lista de números y contar los números pares
for numero in numeros:
    if numero % 2 == 0:
        cantidad_pares += 1

# Imprimir la cantidad de números pares
print("La cantidad de números pares en la lista es:", cantidad_pares)
