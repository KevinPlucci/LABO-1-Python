"""
Escribir un programa que le pida al usuario que ingrese un número entero positivo, y luego imprima "El número es primo" si el número es primo, 
o "El número no es primo" si el número no es primo.
"""
# Solicitar al usuario que ingrese un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Verificar si el número es primo
if numero <= 1:
    print("El número no es primo")
elif numero == 2:
    print("El número es primo")  # 2 es primo
elif numero % 2 == 0:
    print("El número no es primo")  # Si es divisible por 2, no es primo
else:
    print("El número es primo")
