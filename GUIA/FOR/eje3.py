# Dado un número entero n, imprimir la secuencia de números pares menores o iguales a n.

# Solicitar al usuario que ingrese un número entero n
n = int(input("Ingrese un número entero n: "))

# Iterar a través de los números pares menores o iguales a n
print("Secuencia de números pares:")
for numero in range(2, n + 1, 2):
    print(numero)
