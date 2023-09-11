# Crear una función llamada es_alfanumerico que devuelva True en caso de tratarse de solo letras y números y False en el caso contrario (es decir que contenga caracteres especiales)


def es_alfanumerico(cadena):
    # Verificamos si todos los caracteres de la cadena son alfanuméricos
    return cadena.isalnum()


# Ejemplos de uso:
cadena1 = "Alfanumerico123"
print(es_alfanumerico(cadena1))  # Debería devolver True

cadena2 = "Alfanumerico 123"  # Contiene un espacio, no es alfanumérico
print(es_alfanumerico(cadena2))  # Debería devolver False

cadena3 = "CarácterEspecial@1"  # Contiene un carácter especial '@', no es alfanumérico
print(es_alfanumerico(cadena3))  # Debería devolver False
