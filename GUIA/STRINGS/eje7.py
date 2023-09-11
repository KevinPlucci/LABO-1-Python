# Escribir una función que tome un string y devuelva el mismo string con los espacios eliminados


def eliminar_espacios(texto):
    # Usar el método replace para reemplazar espacios con una cadena vacía
    texto_sin_espacios = texto.replace(" ", "")

    # Devolver el string sin espacios
    return texto_sin_espacios


# Ejemplo de uso
texto = "Este es un ejemplo con espacios"
resultado = eliminar_espacios(texto)
print(resultado)
