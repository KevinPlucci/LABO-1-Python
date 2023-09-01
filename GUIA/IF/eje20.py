"""Escribir un programa que le pida al usuario que ingrese dos números enteros, y luego imprima "Los dos números son iguales" si los dos números son iguales, 
"El primer número es mayor" si el primer número es mayor que el segundo, o "El segundo número es mayor" si el segundo número es mayor que el primero."""

# Solicitar al usuario que ingrese dos números enteros
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

# Determinar si los números son iguales o cuál es mayor
if numero1 == numero2:
    print("Los dos números son iguales")
elif numero1 > numero2:
    print("El primer número es mayor")
else:
    print("El segundo número es mayor")
