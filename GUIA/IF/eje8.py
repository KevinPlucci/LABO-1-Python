"""Escribir un programa que le pida al usuario que ingrese un número entero positivo, y luego imprima 
"El número es un cuadrado perfecto" si el número es un cuadrado perfecto,
o "El número no es un cuadrado perfecto" si el número no es un cuadrado perfecto.
"""

# Solicitar al usuario que ingrese un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Verificar si el número es un cuadrado perfecto
if numero < 0:
    print("El número no es un cuadrado perfecto (debe ser positivo)")
else:
    raiz_cuadrada = int(numero**0.5)
    if raiz_cuadrada**2 == numero:
        print("El número es un cuadrado perfecto")
    else:
        print("El número no es un cuadrado perfecto")
