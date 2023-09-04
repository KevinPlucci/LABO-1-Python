# Dado un número entero n, imprimir todos los números impares menores o iguales a n.

# Solicitar al usuario que ingrese un número entero
n = int(input("Ingrese un número entero: "))

# Inicializar un número impar para comenzar
numero_impar = 1

# Imprimir los números impares menores o iguales a n
print("Números impares menores o iguales a", n, ":")

while numero_impar <= n:
    print(numero_impar)
    numero_impar += 2
