"""
Escribir un programa que le pida al usuario que ingrese su edad, y luego imprima 
"Eres mayor de edad" si la edad es mayor o igual a 18, o "Eres menor de edad" si la edad es menor a 18.
"""

# Solicitar al usuario que ingrese su edad
edad = int(input("Ingresa tu edad: "))

# Comprobar si la edad es mayor o igual a 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
