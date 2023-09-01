"""Escribir un programa que le pida al usuario que ingrese un número entero, y luego imprima "El número es múltiplo de 4 y de 6" si el número es múltiplo de 4 y de 6, 
o "El número no es múltiplo de 4 y de 6" si el número no es múltiplo de 4 y de 6.
"""

# Solicitar al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Determinar si el número es múltiplo de 4 y de 6
if numero % 4 == 0 and numero % 6 == 0:
    print("El número es múltiplo de 4 y de 6")
else:
    print("El número no es múltiplo de 4 y de 6")
