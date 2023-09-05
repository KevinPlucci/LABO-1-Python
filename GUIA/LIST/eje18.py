# Solicitar al usuario números enteros hasta que ingrese el 0. Almacenar los números en una lista y luego imprimir el mayor (sin utilizar la función max())

# Crear una lista para almacenar los números ingresados
numeros = []

# Solicitar al usuario números enteros hasta que ingrese 0
while True:
    numero = int(input("Ingrese un número entero (0 para detenerse): "))
    if numero == 0:
        break
    numeros.append(numero)

# Encontrar el mayor número en la lista
if len(numeros) == 0:
    print("No se ingresaron números.")
else:
    mayor = numeros[0]
    for num in numeros:
        if num > mayor:
            mayor = num

    # Imprimir el mayor número
    print("El mayor número ingresado es:", mayor)
