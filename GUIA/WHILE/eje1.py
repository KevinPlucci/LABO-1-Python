# Dado un número entero n, imprimir todos los números desde n hasta 1 en orden descendente.

# Solicitar al usuario que ingrese un número entero
n = int(input("Ingrese un número entero: "))

# Imprimir los números desde n hasta 1 en orden descendente
print("Números desde", n, "hasta 1 en orden descendente:")

while n >= 1:
    print(n)
    n -= 1
