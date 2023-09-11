# Escribir una función que tome dos strings y devuelva un nuevo string que contenga ambos strings concatenados, separados por un espacio.


def concatenar_con_espacio(string1, string2):
    """
    Concatena dos strings con un espacio en medio.

    Args:
        string1 (str): El primer string.
        string2 (str): El segundo string.

    Returns:
        str: El nuevo string con la concatenación de ambos, separados por un espacio.
    """
    return f"{string1} {string2}"


# Ejemplo de uso:
cadena1 = "Hola,"
cadena2 = "mundo!"
resultado = concatenar_con_espacio(cadena1, cadena2)
print(resultado)  # Esto imprimirá: "Hola, mundo!"
