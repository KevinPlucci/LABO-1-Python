# Crea una lista de números enteros y luego encuentra la suma de los números en índices impares.

# Crear una lista de números enteros
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Inicializar una variable para almacenar la suma de los números en índices impares
suma_impares = 0

# Iterar a través de la lista y sumar los números en índices impares
for i in range(len(numeros)):
    if i % 2 != 0:  # Verificar si el índice es impar
        suma_impares += numeros[i]

# Imprimir la suma de los números en índices impares
print("La suma de los números en índices impares es:", suma_impares)
