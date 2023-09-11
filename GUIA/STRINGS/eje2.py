# Escribir una función que reciba un string y devuelva el mismo string todo en minúsculas.


def convertir_a_minusculas(texto):
    """
    Convierte un string a minúsculas.

    Args:
        texto (str): El string que se desea convertir.

    Returns:
        str: El mismo string en minúsculas.
    """
    return texto.lower()


# Ejemplo de uso:
texto_original = "Hola, Esto Es Un Ejemplo."
texto_en_minusculas = convertir_a_minusculas(texto_original)
print(texto_en_minusculas)  # Esto imprimirá: "hola, esto es un ejemplo."
