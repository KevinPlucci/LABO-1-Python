# Dada una lista de números, imprimir la cantidad de números impares en la lista.

# Lista de números
numeros = [5, 10, 7, 2, 8, 15, 3, 12]

# Inicializar la cantidad de números impares
cantidad_impares = 0

# Iterar a través de la lista de números y contar los números impares
for numero in numeros:
    if numero % 2 != 0:
        cantidad_impares += 1

# Imprimir la cantidad de números impares
print("La cantidad de números impares en la lista es:", cantidad_impares)
