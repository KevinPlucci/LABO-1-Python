"""Escribir un programa que le pida al usuario que ingrese su nombre y su edad,
y luego imprima "Eres adolescente" si la edad está entre 13 y 17 inclusive, 
"Eres adulto" si la edad está entre 18 y 64 inclusive, o "Eres adulto mayor" si la edad es mayor o igual a 65.
"""

# Solicitar al usuario que ingrese su nombre
nombre = input("Ingresa tu nombre: ")

# Solicitar al usuario que ingrese su edad
edad = int(input("Ingresa tu edad: "))

# Verificar si la edad es un valor negativo o menor que 13
if edad < 13 or edad < 0:
    print("Dato erróneo")
elif 13 <= edad <= 17:
    print(f"{nombre}, eres adolescente")
elif 18 <= edad <= 64:
    print(f"{nombre}, eres adulto")
else:
    print(f"{nombre}, eres adulto mayor")
