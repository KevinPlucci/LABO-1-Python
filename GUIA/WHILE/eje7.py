# Dada una lista de números, imprimir todos los números que son mayores que el promedio de la lista.

# Lista de números
numeros = [15, 20, 25, 30, 35]

# Calcular el promedio de la lista
promedio = sum(numeros) / len(numeros)

# Imprimir los números mayores que el promedio
print("Números mayores que el promedio:")

# Inicializar un índice para recorrer la lista
indice = 0

while indice < len(numeros):
    if numeros[indice] > promedio:
        print(numeros[indice])
    indice += 1
