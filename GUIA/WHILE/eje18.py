# Dado un número entero n, imprimir la suma de todos los números que son múltiplos de 5 menores o iguales a n.

# Solicitar al usuario que ingrese un número entero n
n = int(input("Ingrese un número entero n: "))

# Inicializar una variable para la suma de múltiplos de 5
suma_multiplos_de_5 = 0

# Inicializar un número para rastrear los múltiplos de 5
numero = 5

# Utilizar un bucle while para sumar los múltiplos de 5 menores o iguales a n
while numero <= n:
    suma_multiplos_de_5 += numero
    numero += 5

# Imprimir la suma de múltiplos de 5
print("La suma de múltiplos de 5 menores o iguales a", n, "es:", suma_multiplos_de_5)
