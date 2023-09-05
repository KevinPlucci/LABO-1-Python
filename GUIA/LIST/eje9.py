"""
Crea una lista de números enteros y pide al usuario que ingrese otro número entero.
Luego, busca el número ingresado en la lista y muestra la posición en la que se encuentra. Si el número no se encuentra en la lista, muestra un mensaje indicando que no se encontró
"""

# Crear una lista de números enteros
numeros = [10, 20, 30, 40, 50]

# Solicitar al usuario que ingrese un número entero
numero_buscar = int(input("Ingrese un número entero para buscar en la lista: "))

# Inicializar una variable para almacenar la posición del número
posicion = -1

# Buscar el número en la lista
for i in range(len(numeros)):
    if numeros[i] == numero_buscar:
        posicion = i
        break

# Comprobar si se encontró el número y mostrar la posición o un mensaje de no encontrado
if posicion != -1:
    print(
        f"El número {numero_buscar} se encuentra en la posición {posicion} de la lista."
    )
else:
    print(f"El número {numero_buscar} no se encontró en la lista.")
