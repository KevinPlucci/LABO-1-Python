"""
Dada una lista de números, 
lista_numeros = [8, 17, 33, 41, 59, 22, 14, 6, 49, 10]
Crea una lista donde los números impares se elevan al cuadrado y los números pares permanecen sin cambios.
"""

lista_numeros = [8, 17, 33, 41, 59, 22, 14, 6, 49, 10]

nueva_lista = [x**2 if x % 2 != 0 else x for x in lista_numeros]

print(nueva_lista)
