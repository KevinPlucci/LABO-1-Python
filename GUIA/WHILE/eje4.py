# Dada una lista de números, imprimir la suma de todos los elementos de la lista.

# Lista de números
numeros = [5, 10, 15, 20, 25]

# Inicializar una variable para almacenar la suma
suma_total = 0

# Índice para recorrer la lista
indice = 0

# Calcular la suma de todos los elementos en la lista usando un bucle while
while indice < len(numeros):
    suma_total += numeros[indice]
    indice += 1

# Imprimir la suma total
print("La suma de todos los elementos en la lista es:", suma_total)
