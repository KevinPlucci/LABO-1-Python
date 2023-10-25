"""
Dada una lista de números: 
lista_numeros = [10, 2, -5, 30, 50]
Crear una nueva lista donde cada número se duplique.
"""

lista_numeros = [10, 2, -5, 30, 50]
nueva_lista = []

for numero in lista_numeros:
    duplicado = numero * 2
    nueva_lista.append(duplicado)

print(nueva_lista)
