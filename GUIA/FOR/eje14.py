# Dado un número entero n, imprimir la secuencia de números perfectos menores o iguales a n.

# Solicitar al usuario que ingrese un número entero
n = int(input("Ingrese un número entero: "))

# Imprimir la secuencia de números perfectos menores o iguales a n
print("Secuencia de números perfectos menores o iguales a", n, ":")

for numero in range(1, n + 1):
    suma_divisores = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma_divisores += divisor

    if suma_divisores == numero:
        print(numero)
