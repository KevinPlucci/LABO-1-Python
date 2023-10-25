"""
Dada una lista de números: 
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Crea una lista que contenga solo los números pares 
"""
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando una comprensión de lista para obtener los números pares
numeros_pares = [numero for numero in lista_numeros if numero % 2 == 0]

print(numeros_pares)
