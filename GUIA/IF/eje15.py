"""Escribir un programa que le pida al usuario que ingrese un número entero positivo,
y luego imprima "El número es primo" si el número es primo, o "El número no es primo" si el número no es primo.
"""

# Solicitar al usuario que ingrese un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Verificar si el número es primo
if numero <= 1:
    print("El número no es primo (debe ser mayor que 1)")
else:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        print("El número es primo")
    else:
        print("El número no es primo")
