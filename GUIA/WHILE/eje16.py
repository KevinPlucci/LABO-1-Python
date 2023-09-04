# Dada una lista de números, imprimir todos los números que son múltiplos de 3.


# Definir una lista de números
lista_de_numeros = [1, 3, 6, 9, 12, 15, 18, 21, 24]

# Inicializar un índice para recorrer la lista
indice = 0

# Imprimir todos los números que son múltiplos de 3
print("Números que son múltiplos de 3:")

while indice < len(lista_de_numeros):
    numero = lista_de_numeros[indice]
    if numero % 3 == 0:
        print(numero)
    indice += 1
