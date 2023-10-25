"""
Genera una lista que contenga 10 números enteros aleatorios en un rango del 1 al 1000.
"""

import random

# Genera una lista de 10 números enteros aleatorios en el rango del 1 al 1000
lista_numeros = [random.randint(1, 1000) for _ in range(10)]

print(lista_numeros)
