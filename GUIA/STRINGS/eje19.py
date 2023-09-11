# Escribir una función que tome una cadena de caracteres y cuente la cantidad de dígitos que contiene, por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.


def contar_digitos(cadena):
    # Inicializar un contador de dígitos
    contador = 0

    # Recorrer la cadena de caracteres
    for caracter in cadena:
        # Verificar si el caracter es un dígito
        if caracter.isdigit():
            contador += 1

    return contador


# Ejemplo de uso
cadena = "1234 Hola Mundo"
cantidad_de_digitos = contar_digitos(cadena)
print(f"La cadena '{cadena}' contiene {cantidad_de_digitos} dígitos.")
