"""Escribir un programa que le pida al usuario que ingrese un número entero, y luego imprima "El número es par y es múltiplo de 3" si el número es par y es múltiplo de 3, 
o "El número no cumple ninguna de las dos condiciones" si el número no cumple ninguna de las dos condiciones.
"""

# Solicitar al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Determinar si el número es par y múltiplo de 3
if numero % 2 == 0 and numero % 3 == 0:
    print("El número es par y es múltiplo de 3")
else:
    print("El número no cumple ninguna de las dos condiciones")
