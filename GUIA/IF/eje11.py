"""Escribir un programa que le pida al usuario que ingrese su edad, y luego imprima "Eres un niño" 
si la edad es menor a 12, "Eres un adolescente" si la edad está entre 12 y 17 inclusive, "Eres un adulto" si la edad está entre 18 y 64
"""
# Solicitar al usuario que ingrese su edad
edad = int(input("Ingresa tu edad: "))

# Determinar si el usuario es un niño, un adolescente o un adulto
if edad < 12:
    print("Eres un niño")
elif 12 <= edad <= 17:
    print("Eres un adolescente")
elif 18 <= edad <= 64:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")
