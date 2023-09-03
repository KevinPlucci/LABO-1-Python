# Dada una lista de números, imprimir la suma de los números en la lista que son mayores que el promedio de la lista.

# Lista de números
numeros = [12, 8, 15, 6, 20, 10]

# Calcular el promedio de la lista
promedio = sum(numeros) / len(numeros)

# Inicializar la suma de los números mayores que el promedio
suma_mayores_que_promedio = 0

# Iterar a través de la lista y sumar los números mayores que el promedio
for numero in numeros:
    if numero > promedio:
        suma_mayores_que_promedio += numero

# Imprimir la suma de los números mayores que el promedio
print("La suma de los números mayores que el promedio es:", suma_mayores_que_promedio)
