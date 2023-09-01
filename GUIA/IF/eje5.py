"""
Escribir un programa que le pida al usuario que ingrese su nombre, y luego imprima 
"Hola [nombre]" si el nombre ingresado es "Juan", "María" o "Pedro", o "Hola desconocido" si el nombre ingresado no es uno de esos tres.
"""

# Solicitar al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")

# Comprobar si el nombre es "Juan", "María" o "Pedro"
if nombre == "Juan" or nombre == "María" or nombre == "Pedro":
    print(f"Hola {nombre}")
else:
    print("Hola desconocido")
