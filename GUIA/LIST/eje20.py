# A partir de la lista: [1,80,5,0,15,-5,1,79] determinar, el mayor, el menor, el promedio y la suma total de todos los elementos

# Lista de números
numeros = [1, 80, 5, 0, 15, -5, 1, 79]

# Encontrar el mayor número
mayor = numeros[0]
for numero in numeros:
    if numero > mayor:
        mayor = numero

# Encontrar el menor número
menor = numeros[0]
for numero in numeros:
    if numero < menor:
        menor = numero

# Calcular la suma total
suma_total = sum(numeros)

# Calcular el promedio
promedio = suma_total / len(numeros)

# Imprimir los resultados
print("El mayor número en la lista es:", mayor)
print("El menor número en la lista es:", menor)
print("La suma total de los elementos es:", suma_total)
print("El promedio de los elementos es:", promedio)
