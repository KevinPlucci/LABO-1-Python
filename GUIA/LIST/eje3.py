# Crea una lista vacía y pide al usuario que ingrese números enteros hasta que ingrese un número negativo. Luego, muestra la suma de todos los números ingresados.

# Crear una lista vacía para almacenar los números ingresados
numeros = []

# Solicitar al usuario que ingrese números enteros hasta que ingrese un número negativo
while True:
    numero = int(
        input("Ingrese un número entero (ingrese un número negativo para finalizar): ")
    )
    if numero < 0:
        break  # Salir del bucle si se ingresa un número negativo
    numeros.append(numero)

# Calcular la suma de los números ingresados
suma = sum(numeros)

# Mostrar la suma de los números ingresados
print(f"La suma de los números ingresados es: {suma}")
