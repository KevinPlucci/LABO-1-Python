# Dado un número entero n, imprimir la secuencia de números triangulares menores o iguales a n.

# Solicitar al usuario que ingrese un número entero
n = int(input("Ingrese un número entero: "))

# Inicializar variables
suma = 0

# Imprimir la secuencia de números triangulares menores o iguales a n
print("Secuencia de números triangulares menores o iguales a", n, ":")

for numero_triangular in range(1, n + 1):
    suma += numero_triangular
    if suma <= n:
        print(numero_triangular)
    else:
        break
