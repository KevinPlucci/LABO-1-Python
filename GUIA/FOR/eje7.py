# Dado un número entero n, imprimir la secuencia de números impares menores o iguales a n.

# Solicitar al usuario que ingrese un número entero
n = int(input("Ingrese un número entero: "))

# Imprimir la secuencia de números impares menores o iguales a n
print("Secuencia de números impares menores o iguales a", n, ":")

for i in range(1, n + 1, 2):
    print(i)
