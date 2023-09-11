# Crear una función llamada es_solo_texto que reciba un string y devuelva True en caso de que trate solo de caracteres alfabéticos y el espacio y False en el caso contrario


def es_solo_texto(texto):
    # Iteramos por cada carácter en el texto
    for caracter in texto:
        # Verificamos si el carácter no es una letra ni un espacio
        if not (caracter.isalpha() or caracter.isspace()):
            return False
    # Si hemos recorrido todo el texto sin encontrar caracteres no deseados, devolvemos True
    return True


# Ejemplos de uso:
texto1 = "Texto con letras y espacios"
print(es_solo_texto(texto1))  # Debería devolver True

texto2 = "12345"
print(es_solo_texto(texto2))  # Debería devolver False

texto3 = "Texto con números 123"
print(es_solo_texto(texto3))  # Debería devolver False

texto4 = "Texto con signos: !?¿"
print(es_solo_texto(texto4))  # Debería devolver False
