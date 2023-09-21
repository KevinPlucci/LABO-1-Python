# Dado un numero entero n, imprimir todos los numeros desde 1 hasta n en orden ascendente

numero_texto = input("Ingrese un numero: ")
# VALIDAR
numero_int = int(numero_texto)
contador = 1
while contador < numero_int:
    print(contador)
    contador = contador + 1  # contado += 1
