# Escribir una función que tome un string y un carácter y devuelva una lista con todas las palabras en el string que contienen ese carácter.


def palabras_con_caracter(texto, caracter):
    # Dividir el texto en palabras usando espacio como separador
    palabras = texto.split()

    # Inicializar una lista para almacenar las palabras que contienen el carácter
    palabras_con_caracter = []

    # Iterar a través de cada palabra en la lista de palabras
    for palabra in palabras:
        # Verificar si el carácter está presente en la palabra
        if caracter in palabra:
            # Si el carácter está presente, agregar la palabra a la lista
            palabras_con_caracter.append(palabra)

    # Devolver la lista de palabras que contienen el carácter
    return palabras_con_caracter


# Ejemplo de uso
texto = "Este es un ejemplo de una función que busca palabras con la letra 'a'"
caracter = "a"
resultado = palabras_con_caracter(texto, caracter)
print(resultado)
