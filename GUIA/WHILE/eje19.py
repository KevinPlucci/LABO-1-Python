# Dada una lista de números, imprimir todos los números que son mayores que el número anterior en la lista.

lista_de_numeros = [1, 3, 5, 2, 7, 6, 8, 4]

# Inicializa un índice en 1 para empezar desde el segundo elemento.
indice = 1

while indice < len(lista_de_numeros):
    # Comprueba si el número actual es mayor que el número anterior en la lista.
    if lista_de_numeros[indice] > lista_de_numeros[indice - 1]:
        # Si es mayor, imprímelo.
        print(lista_de_numeros[indice])

    # Incrementa el índice para pasar al siguiente elemento en la lista.
    indice += 1
