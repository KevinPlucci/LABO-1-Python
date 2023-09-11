# Escribir una función que tome un string y un carácter y devuelva el número de veces que aparece ese carácter en el string.


def contar_caracteres_en_string(texto, caracter):
    """
    Cuenta el número de veces que un carácter aparece en un string.

    Args:
        texto (str): El string en el que se busca el carácter.
        caracter (str): El carácter que se desea contar en el string.

    Returns:
        int: El número de veces que el carácter aparece en el string.
    """
    contador = 0
    for char in texto:
        if char == caracter:
            contador += 1
    return contador


# Ejemplo de uso:
cadena = "Hola, mundo!"
caracter_a_contar = "o"
veces_que_aparece = contar_caracteres_en_string(cadena, caracter_a_contar)
print(
    f"El carácter '{caracter_a_contar}' aparece {veces_que_aparece} veces."
)  # Esto imprimirá: "El carácter 'o' aparece 2 veces."
