# Dado un número entero n, imprimir todos los números desde 1 hasta n en orden ascendente.

# Solicitar al usuario que ingrese un número entero
n = int(input("Ingrese un número entero: "))

# Inicializar una variable para el contador
contador = 1

# Imprimir los números desde 1 hasta n en orden ascendente
print("Números desde 1 hasta", n, "en orden ascendente:")

while contador <= n:
    print(contador)
    contador += 1
