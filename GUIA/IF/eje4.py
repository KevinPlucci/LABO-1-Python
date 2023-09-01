"""
Escribir un programa que le pida al usuario que ingrese dos números enteros, y luego imprima "El primer número es mayor"
si el primer número es mayor que el segundo, "El segundo número es mayor" si el segundo número es mayor que el primero, o "Los dos números son iguales"
si los dos números son iguales
"""

# Solicitar al usuario que ingrese dos números enteros
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

# Comparar los dos números e imprimir el resultado
if numero1 > numero2:
    print("El primer número es mayor")
elif numero2 > numero1:
    print("El segundo número es mayor")
else:
    print("Los dos números son iguales")
