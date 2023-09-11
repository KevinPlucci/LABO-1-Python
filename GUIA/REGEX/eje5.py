# Crear una función llamada es_decimal que reciba dos strings: el primero representa la expresión a evaluar y el segundo el separador decimal (puede ser punto . o coma ,).
# Debe devolver True en caso que se trate de un número decimal y False en el caso contrario.


def es_decimal(expresion, separador_decimal):
    try:
        # Reemplazamos el separador decimal por un punto para asegurarnos de que Python lo reconozca
        expresion = expresion.replace(separador_decimal, ".")

        # Intentamos convertir la expresión a un número decimal (float)
        float(expresion)

        # Si no se produjo una excepción al convertir, es un número decimal válido
        return True
    except ValueError:
        # Si se produce una excepción al convertir, no es un número decimal válido
        return False


# Ejemplos de uso:
expresion1 = "3.14"
separador1 = "."
print(es_decimal(expresion1, separador1))  # Debería devolver True

expresion2 = "123,45"
separador2 = ","
print(es_decimal(expresion2, separador2))  # Debería devolver True

expresion3 = "abc"
separador3 = "."
print(es_decimal(expresion3, separador3))  # Debería devolver False

expresion4 = "12.34.56"
separador4 = "."
print(es_decimal(expresion4, separador4))  # Debería devolver False
