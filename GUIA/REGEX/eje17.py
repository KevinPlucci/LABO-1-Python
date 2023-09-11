# Crear la función validar_patente que reciba un string como parámetro y devuelva True en caso de tratarse de un número de patente válido o False en caso contrario.
# Debe poder admitir estos dos tipos:

import re


def validar_patente(patente):
    # Patrón para el primer tipo de patente (7 caracteres, 2 letras, 3 números, 2 letras)
    patron_tipo1 = r"^[A-Z]{2}\d{3}[A-Z]{2}$"

    # Patrón para el segundo tipo de patente (6 caracteres, 3 letras, 3 números)
    patron_tipo2 = r"^[A-Z]{3}\d{3}$"

    if re.match(patron_tipo1, patente) or re.match(patron_tipo2, patente):
        return True
    else:
        return False


# Ejemplos de uso
print(validar_patente("AA123BB"))  # True (Tipo 1)
print(validar_patente("ABC123"))  # True (Tipo 1)
print(validar_patente("ABC1234"))  # False
print(validar_patente("123ABC"))  # False
print(validar_patente("ABC123C"))  # False
print(validar_patente("ABC123D"))  # False
print(validar_patente("XYZ456"))  # True (Tipo 2)
print(validar_patente("123XYZ"))  # False (Tipo 2)
