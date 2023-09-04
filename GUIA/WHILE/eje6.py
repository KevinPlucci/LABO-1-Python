# Dado un número entero n, imprimir la suma de todos los números pares menores o iguales a n.

# Solicitar al usuario que ingrese un número entero
n = int(input("Ingrese un número entero: "))

# Inicializar la suma de los números pares
suma_pares = 0

# Inicializar un número par para comenzar
numero_par = 2

# Calcular la suma de los números pares menores o iguales a n usando un bucle while
while numero_par <= n:
    suma_pares += numero_par
    numero_par += 2

# Imprimir la suma de los números pares
print("La suma de los números pares menores o iguales a", n, "es:", suma_pares)
