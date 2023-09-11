# Crear la función es_fecha que reciba dos string, el primero representa la expresión a evaluar y el segundo el separador de la fecha (puede ser la barra / o el guión -)
# y que devuelva True en caso de tratarse de una fecha válida y False en el caso contrario. Los formatos admitidos son: ‘dd/mm/aaaa’ o ‘dd-mm-aaaa’

import re
from datetime import datetime


def es_fecha(expresion, separador):
    # Definimos patrones de expresiones regulares para los dos formatos de fecha
    patrones = [
        r"\d{2}" + re.escape(separador) + r"\d{2}" + re.escape(separador) + r"\d{4}",
        r"\d{2}" + re.escape(separador) + r"\d{2}" + re.escape(separador) + r"\d{4}",
    ]

    # Comprobamos si la expresión coincide con alguno de los patrones
    for patron in patrones:
        if re.fullmatch(patron, expresion):
            # Si coincide con un patrón, intentamos convertirlo en una fecha
            try:
                fecha = datetime.strptime(
                    expresion, "%d" + separador + "%m" + separador + "%Y"
                )
                return True
            except ValueError:
                # Si la conversión falla, no es una fecha válida
                return False

    # Si no coincide con ninguno de los patrones, no es una fecha válida
    return False


# Ejemplos de uso:
fecha1 = "15/09/2023"
separador1 = "/"
print(es_fecha(fecha1, separador1))  # Debería devolver True

fecha2 = "30-02-2022"  # Fecha inválida (febrero no tiene 30 días)
separador2 = "-"
print(es_fecha(fecha2, separador2))  # Debería devolver False

fecha3 = "12/25/2023"  # Formato incorrecto (mes 25)
separador3 = "/"
print(es_fecha(fecha3, separador3))  # Debería devolver False

fecha4 = "01-01-99"  # Año con solo dos dígitos
separador4 = "-"
print(es_fecha(fecha4, separador4))  # Debería devolver False
