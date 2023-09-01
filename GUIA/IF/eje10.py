"""Escribir un programa que le pida al usuario que ingrese un número entero, y luego imprima "El número es positivo y par" si el número es positivo y divisible por 2,
o "El número no cumple ninguna condición" si el número no cumple ninguna de las dos condiciones anteriores
"""

# Solicitar al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Verificar si el número es positivo y divisible por 2
if numero > 0 and numero % 2 == 0:
    print("El número es positivo y par")
else:
    print("El número no cumple ninguna condición")
