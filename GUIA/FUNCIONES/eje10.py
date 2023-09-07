# Crea una función que reciba como parámetros una lista de palabras y devuelva la palabra más larga.


def palabra_mas_larga(lista_palabras):
    if not lista_palabras:
        return None  # Si la lista está vacía, retornamos None

    palabra_mas_larga = lista_palabras[0]  # Inicializamos con la primera palabra

    for palabra in lista_palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra

    return palabra_mas_larga


# Ejemplo de uso
palabras = ["gato", "perro", "elefante", "ratón"]
resultado = palabra_mas_larga(palabras)
print(f"La palabra más larga es: {resultado}")
