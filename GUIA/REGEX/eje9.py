# Crear una función que reciba un texto y devuelva una lista con las palabras que contienen entre 3 y 6 caracteres de largo


def palabras_entre_3_y_6_caracteres(texto):
    # Dividimos el texto en palabras
    palabras = texto.split()

    # Utilizamos una comprensión de lista para filtrar las palabras con 3 a 6 caracteres
    palabras_filtradas = [palabra for palabra in palabras if 3 <= len(palabra) <= 6]

    return palabras_filtradas


# Ejemplo de uso:
texto = "Esta es una frase de ejemplo con palabras cortas y largas"
resultado = palabras_entre_3_y_6_caracteres(texto)
print(resultado)  # Debería devolver ['una', 'frase', 'con', 'y']
