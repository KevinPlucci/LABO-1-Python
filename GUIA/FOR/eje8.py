# Dado un número entero n, imprimir la suma de los números pares menores o iguales a n.

# Solicitar al usuario que ingrese un número entero
n = int(input("Ingrese un número entero: "))

# Inicializar la suma
suma_pares = 0

# Calcular la suma de números pares menores o iguales a n
for i in range(2, n + 1, 2):
    suma_pares += i

# Imprimir la suma de números pares
print("La suma de números pares menores o iguales a", n, "es:", suma_pares)
