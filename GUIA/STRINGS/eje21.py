# Crear una función que reciba como parámetro un string y devuelva un diccionario donde cada clave es una palabra y cada valor es un entero que indica cuántas veces aparece esa palabra dentro del string.


def contar_palabras(string):
    # Dividir el string en palabras usando espacio como separador
    palabras = string.split()

    # Inicializar un diccionario vacío para almacenar el conteo de palabras
    conteo_palabras = {}

    # Iterar a través de las palabras y contar su frecuencia
    for palabra in palabras:
        # Eliminar signos de puntuación alrededor de la palabra (si es necesario)
        palabra = palabra.strip(".,!?:;\"'")

        # Convertir la palabra a minúsculas para hacer el conteo insensible a mayúsculas y minúsculas
        palabra = palabra.lower()

        # Incrementar el contador de la palabra en el diccionario
        if palabra in conteo_palabras:
            conteo_palabras[palabra] += 1
        else:
            conteo_palabras[palabra] = 1

    return conteo_palabras


# Ejemplo de uso
texto = "Este es un ejemplo de un texto. Un texto es una secuencia de palabras."
resultado = contar_palabras(texto)
print(resultado)
