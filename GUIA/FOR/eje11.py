# Dado un número entero n, imprimir la secuencia de números primos menores o iguales a n.

# Solicitar al usuario que ingrese un número entero
n = int(input("Ingrese un número entero: "))

# Imprimir la secuencia de números primos menores o iguales a n
print("Secuencia de números primos menores o iguales a", n, ":")

for numero in range(2, n + 1):
    es_primo = True
    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(numero)
