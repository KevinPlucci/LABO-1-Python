# Crear una función llamada es_entero que reciba un string y devuelva True en caso de que se trate de un número entero y False en caso contrario.


def es_entero(texto):
    # Verificamos si el string está vacío
    if len(texto) == 0:
        return False

    # Verificamos si el primer carácter es un signo '-' o '+'
    if texto[0] in ("-", "+"):
        # Si es un número negativo o positivo, comprobamos si el resto de los caracteres son dígitos
        return texto[1:].isdigit()

    # Si no tiene signo, comprobamos si todos los caracteres son dígitos
    return texto.isdigit()


# Ejemplos de uso:
texto1 = "12345"
print(es_entero(texto1))  # Debería devolver True

texto2 = "-6789"
print(es_entero(texto2))  # Debería devolver True

texto3 = "+42"
print(es_entero(texto3))  # Debería devolver True

texto4 = "12.34"
print(es_entero(texto4))  # Debería devolver False

texto5 = "abc123"
print(es_entero(texto5))  # Debería devolver False
