# Escribir una función que tome un número binario y lo convierta en una cadena de 8 bits, rellenando con ceros a la izquierda si es necesario, por ejemplo: "101" -> "00000101".


def binario_a_8bits(numero_binario):
    # Obtener la longitud actual del número binario
    longitud_actual = len(numero_binario)

    # Calcular cuántos ceros se deben agregar
    ceros_a_agregar = 8 - longitud_actual

    # Construir la cadena de 8 bits con ceros a la izquierda
    cadena_8bits = "0" * ceros_a_agregar + numero_binario

    return cadena_8bits


# Ejemplo de uso
numero_binario = "101"
cadena_8bits = binario_a_8bits(numero_binario)
print(cadena_8bits)  # Debería imprimir "00000101"
