"""
Dada esta lista:
lista_numeros = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6]
Crea una lista que contenga solo los valores únicos 
"""

lista_numeros = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6]
lista_unica = []

for numero in lista_numeros:
    if numero not in lista_unica:
        lista_unica.append(numero)

print(lista_unica)
