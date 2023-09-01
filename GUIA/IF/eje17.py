"""Escribir un programa que le pida al usuario que ingrese un número entero, y luego imprima "El número es negativo" si el número es menor que cero, 
"El número es cero" si el número es igual a cero, o "El número es positivo" si el número es mayor que cero.
"""

# Solicitar al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Determinar si el número es negativo, igual a cero o positivo
if numero < 0:
    print("El número es negativo")
elif numero == 0:
    print("El número es cero")
else:
    print("El número es positivo")
