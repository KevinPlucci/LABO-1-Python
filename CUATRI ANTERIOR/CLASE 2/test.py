# Escribir un programa que le pida al usuario que ingrese un numero entero,
# y luego imprima "El numero ingresado es par" si el numero es divisible
# por 2, o el "El numero ingresado es impar" si el numero no es divisble por 2

numero_texto = input("Ingrese un numero: ")
# VALIDAR
numero_int = int(numero_texto)
resto = numero_int % 2
if resto == 0:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")

if int(numero_texto) % 2 == 0:
    print("EL numero ingresado es par")
else:
    print("El numero ingresado es impar")
