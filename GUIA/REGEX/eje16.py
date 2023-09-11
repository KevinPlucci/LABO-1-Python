# Crear la función validar_codigo_postal que reciba un string como parámetro y devuelva True en caso de tratarse de código postal válido o False en caso contrario.

import re


def validar_codigo_postal(codigo_postal):
    # Expresión regular para el formato de código postal con territorio y cara de manzana
    patron_cpa = r"^[A-Z0-9]{5}\s[A-Z]{3}$"

    # Verificar si el código postal coincide con el patrón
    if re.match(patron_cpa, codigo_postal):
        return True
    else:
        return False


# Ejemplos de uso
codigo1 = "B1636 FDA"
codigo2 = "C2750 XYZ"
codigo3 = "98765"
print(validar_codigo_postal(codigo1))  # True
print(validar_codigo_postal(codigo2))  # True
print(validar_codigo_postal(codigo3))  # False
