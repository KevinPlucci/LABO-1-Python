# Escribir una función que tome una cadena de caracteres y reemplace todas las letras mayúsculas por letras minúsculas y todas las letras minúsculas por letras mayúsculas, por ejemplo: "HoLa" -> "hOlA"


def intercambiar_mayusculas_y_minusculas(cadena):
    # Usar el método swapcase() para intercambiar mayúsculas y minúsculas
    resultado = cadena.swapcase()

    return resultado


# Ejemplo de uso
cadena = "HoLa"
cadena_transformada = intercambiar_mayusculas_y_minusculas(cadena)
print(cadena_transformada)  # Debería imprimir "hOlA"
