# Escribir una función que reciba un string y devuelva el mismo string todo en mayúsculas.


def convertir_a_mayusculas(texto):
    """
    Convierte un string a mayúsculas.

    Args:
        texto (str): El string que se desea convertir.

    Returns:
        str: El mismo string en mayúsculas.
    """
    return texto.upper()


# Ejemplo de uso:
texto_original = "Hola, esto es un ejemplo."
texto_en_mayusculas = convertir_a_mayusculas(texto_original)
print(texto_en_mayusculas)  # Esto imprimirá: "HOLA, ESTO ES UN EJEMPLO."
