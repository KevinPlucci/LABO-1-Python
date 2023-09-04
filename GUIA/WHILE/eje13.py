# Dada una lista de números, imprimir la cantidad de números negativos en la lista.

# Definir una lista de números
lista_de_numeros = [1, -2, 3, -4, 5, -6, 7, -8, 9]

# Inicializar una variable para contar los números negativos y un índice
cantidad_de_negativos = 0
indice = 0

# Usar un bucle while para contar los números negativos
while indice < len(lista_de_numeros):
    if lista_de_numeros[indice] < 0:
        cantidad_de_negativos += 1
    indice += 1

# Imprimir la cantidad de números negativos
print("La cantidad de números negativos en la lista es:", cantidad_de_negativos)
