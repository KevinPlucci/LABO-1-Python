""""
Escribir un programa que le pida al usuario que ingrese un número entero positivo, y luego imprima "El número ingresado es positivo" 
si el número es mayor que cero, o "El número ingresado es cero o negativo" si el número es menor o igual a cero.
"""

# Solicitar al usuario que ingrese un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Comprobar si el número es mayor que cero
if numero > 0:
    print("El número ingresado es positivo")
else:
    print("El número ingresado es cero o negativo")
