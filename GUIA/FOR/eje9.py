# Dada una lista de números, imprimir la cantidad de números negativos en la lista.

# Lista de números
numeros = [5, -2, 10, -7, 0, -3]

# Inicializar la cantidad de números negativos
cantidad_negativos = 0

# Iterar a través de la lista de números y contar los negativos
for numero in numeros:
    if numero < 0:
        cantidad_negativos += 1

# Imprimir la cantidad de números negativos
print("La cantidad de números negativos en la lista es:", cantidad_negativos)
