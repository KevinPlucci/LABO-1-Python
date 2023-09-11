# Crear una función llamada es_binario que devuelva True en caso de un número binario válido (solo ceros y unos) o False en el caso contrario


def es_binario(cadena):
    # Iteramos por cada carácter en la cadena
    for caracter in cadena:
        # Verificamos si el carácter no es ni "0" ni "1"
        if caracter != "0" and caracter != "1":
            return False
    # Si hemos recorrido toda la cadena sin encontrar caracteres no deseados, devolvemos True
    return True


# Ejemplos de uso:
cadena1 = "101010"
print(es_binario(cadena1))  # Debería devolver True

cadena2 = "1102"  # Contiene el dígito "2", no es binario válido
print(es_binario(cadena2))  # Debería devolver False

cadena3 = "00001111"
print(es_binario(cadena3))  # Debería devolver True

cadena4 = "ABCDE"  # Contiene letras, no es binario válido
print(es_binario(cadena4))  # Debería devolver False
