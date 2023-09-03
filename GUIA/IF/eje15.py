"""Escribir un programa que le pida al usuario que ingrese un número entero positivo,
y luego imprima "El número es primo" si el número es primo, o "El número no es primo" si el número no es primo.
"""

# Solicitar al usuario que ingrese un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Verificar si el número es menor o igual a 1
if numero <= 0:
    print("El número no es positivo")
elif numero == 1:
    print("El número no es primo")  # 1 no es considerado primo
elif numero == 2:
    print("El número es primo")  # 2 es primo
else:
    es_primo = True  # Suponemos que el número es primo inicialmente
    divisor = 2

    if numero % divisor == 0:
        es_primo = False  # Si es divisible, el número no es primo

    # Imprimir el resultado
    if es_primo:
        print("El número es primo")
    else:
        print("El número no es primo")
