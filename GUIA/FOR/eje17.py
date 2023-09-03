# Dado un número entero n, imprimir la secuencia de números de Harshad menores o iguales a n.

# Solicitar al usuario que ingrese un número entero
n = int(input("Ingrese un número entero: "))

# Imprimir la secuencia de números de Harshad menores o iguales a n
print("Secuencia de números de Harshad menores o iguales a", n, ":")

for numero in range(1, n + 1):
    suma_digitos = 0
    num = numero
    while num > 0:
        suma_digitos += num % 10
        num //= 10
    if numero % suma_digitos == 0:
        print(numero)
