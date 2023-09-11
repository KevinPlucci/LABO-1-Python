# Escribir una función que tome un string y devuelva el número de caracteres que tiene el string.


def contar_caracteres(texto):
    """
    Cuenta el número de caracteres en un string.

    Args:
        texto (str): El string del cual se desea contar los caracteres.

    Returns:
        int: El número de caracteres en el string.
    """
    return len(texto)


# Ejemplo de uso:
cadena = "¡Hola, mundo!"
numero_de_caracteres = contar_caracteres(cadena)
print(numero_de_caracteres)  # Esto imprimirá: 12
