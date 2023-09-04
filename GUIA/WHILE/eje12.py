# Dado un número entero n, imprimir la suma de todos los números impares menores o iguales a n.

# Solicitar al usuario que ingrese un número entero n
n = int(input("Ingrese un número entero n: "))

# Inicializar una variable para almacenar la suma de números impares
suma_impares = 0

# Inicializar un contador en 1
contador = 1

# Usar un bucle while para sumar números impares menores o iguales a n
while contador <= n:
    if contador % 2 != 0:
        suma_impares += contador
    contador += 1

# Imprimir la suma de números impares
print("La suma de números impares menores o iguales a", n, "es:", suma_impares)
