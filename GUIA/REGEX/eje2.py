# Crear una función llamada es_minuscula que reciba un string y devuelva True en caso de que todas las letras sean mayúsculas o False en el caso contrario


def es_minuscula(texto):
    # Iteramos por cada carácter en el texto
    for caracter in texto:
        # Si cualquier carácter no es una letra minúscula, devolvemos False
        if not caracter.islower():
            return False
    # Si hemos recorrido todo el texto sin encontrar mayúsculas, devolvemos True
    return True


# Ejemplos de uso:
texto1 = "todaslasletrassonminusculas"
print(es_minuscula(texto1))  # Debería devolver True

texto2 = "Alguna Letra En Mayúscula"
print(es_minuscula(texto2))  # Debería devolver False
