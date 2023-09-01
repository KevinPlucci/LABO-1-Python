"""Escribir un programa que le pida al usuario que ingrese dos números enteros, 
y luego imprima "El primer número es positivo" si el primer número es mayor que cero, 
"El segundo número es positivo" si el segundo número es mayor que cero, o "Ambos números son negativos" si los dos números son negativos.
"""

# Solicitar al usuario que ingrese dos números enteros
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

# Determinar si los números son positivos o negativos
if numero1 > 0:
    print("El primer número es positivo")
elif numero2 > 0:
    print("El segundo número es positivo")
else:
    print("Ambos números son negativos")
