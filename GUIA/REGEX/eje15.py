# Crear la función es_hora que reciba un string y que devuelva True en caso de tratarse de una hora válida y False en el caso contrario. El formato admitido es ‘hh:mm:ss’

import re


def es_hora(expresion):
    # Patrón de expresión regular para el formato 'hh:mm:ss'
    patron = r"^[0-2][0-9]:[0-5][0-9]:[0-5][0-9]$"

    # Comprobamos si la expresión coincide con el patrón
    if re.fullmatch(patron, expresion):
        # Dividimos la expresión en horas, minutos y segundos
        horas, minutos, segundos = map(int, expresion.split(":"))

        # Validamos las partes de la hora
        if 0 <= horas <= 23 and 0 <= minutos <= 59 and 0 <= segundos <= 59:
            return True

    # Si no coincide con el patrón o las partes de la hora no son válidas, no es una hora válida
    return False


# Ejemplos de uso:
hora1 = "12:34:56"
print(es_hora(hora1))  # Debería devolver True

hora2 = "25:61:99"  # Horas, minutos o segundos fuera de rango
print(es_hora(hora2))  # Debería devolver False

hora3 = "abc:def:ghi"  # Formato incorrecto
print(es_hora(hora3))  # Debería devolver False

hora4 = "09:30:00"
print(es_hora(hora4))  # Debería devolver True
