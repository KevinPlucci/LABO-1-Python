# Crea dos listas de 10 números enteros cada una y realiza una multiplicación de los elementos con el mismo índice en ambas listas.

# Crear dos listas de 10 números enteros cada una
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Crear una lista para almacenar los resultados de la multiplicación
resultado = []

# Realizar la multiplicación de los elementos con el mismo índice
for i in range(len(lista1)):
    multiplicacion = lista1[i] * lista2[i]
    resultado.append(multiplicacion)

# Imprimir la lista de resultados
print("Resultado de la multiplicación de las listas:")
print(resultado)
