# Crear una función que recibe una lista de palabras y devuelve un diccionario con las palabras como llaves y su longitud como valores.


def palabras_a_diccionario(lista_palabras):
    diccionario = {}
    for palabra in lista_palabras:
        diccionario[palabra] = len(palabra)
    return diccionario


# Ejemplo de uso
palabras = ["gato", "perro", "elefante", "ratón"]
resultado = palabras_a_diccionario(palabras)
print(resultado)
