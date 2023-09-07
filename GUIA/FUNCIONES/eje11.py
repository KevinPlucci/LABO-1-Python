# Crea una función que reciba como parámetro una cadena de texto y devuelva la cantidad de vocales que tiene.


def contar_vocales(cadena):
    # Convertimos la cadena a minúsculas para tratar las vocales tanto en mayúsculas como en minúsculas
    cadena = cadena.lower()

    # Definimos una lista de vocales
    vocales = "aeiou"

    # Inicializamos un contador
    contador = 0

    # Recorremos la cadena de texto
    for caracter in cadena:
        if caracter in vocales:
            contador += 1

    return contador


# Ejemplo de uso
texto = "Hola, ¿cómo estás?"
cantidad_vocales = contar_vocales(texto)
print(f"La cantidad de vocales en la cadena es: {cantidad_vocales}")
