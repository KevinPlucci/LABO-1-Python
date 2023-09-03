# Dado un número entero n, imprimir la suma de los números impares menores o iguales a n.

# Solicitar al usuario que ingrese un número entero n
n = int(input("Ingrese un número entero n: "))

# Inicializar una variable para almacenar la suma
suma_impares = 0

# Iterar a través de los números impares menores o iguales a n
for numero in range(1, n + 1, 2):
    suma_impares += numero

# Imprimir la suma de los números impares
print("La suma de los números impares menores o iguales a", n, "es:", suma_impares)
