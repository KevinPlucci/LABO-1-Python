# Dado un número entero n, imprimir todos los números primos menores o iguales a n.

# Solicitar al usuario que ingrese un número entero n
n = int(input("Ingrese un número entero n: "))

# Imprimir todos los números primos menores o iguales a n
print("Números primos menores o iguales a", n, ":")

numero = 2

while numero <= n:
    es_primo = True
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            es_primo = False
            break
        divisor += 1
    if es_primo:
        print(numero)
    numero += 1
