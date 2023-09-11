# Crear una función llamada es_mayuscula que reciba un string y devuelva True en caso de que todas las letras sean mayúsculas o False en el caso contrario


def es_mayuscula(texto):
    # Iteramos por cada carácter en el texto
    for caracter in texto:
        # Si cualquier carácter no es una letra mayúscula, devolvemos False
        if not caracter.isupper():
            return False
    # Si hemos recorrido todo el texto sin encontrar minúsculas, devolvemos True
    return True


# Ejemplos de uso:
texto1 = "TODASLASLETRASSONMAYUSCULAS"
print(es_mayuscula(texto1))  # Debería devolver True

texto2 = "Alguna Letra En Minúscula"
print(es_mayuscula(texto2))  # Debería devolver False
