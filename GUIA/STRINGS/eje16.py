# Escribir una función que tome una cadena de texto y la convierta en un acrónimo, tomando la primera letra de cada palabra, por ejemplo: "Universidad Tecnológica Nacional Facultad Regional Avellaneda" -> "UTNFRA”.


def generar_acronimo(cadena):
    # Dividir la cadena en palabras
    palabras = cadena.split()

    # Inicializar una cadena vacía para el acrónimo
    acronimo = ""

    # Recorrer las palabras y tomar la primera letra de cada una
    for palabra in palabras:
        acronimo += palabra[0]

    # Convertir el acrónimo a mayúsculas
    acronimo = acronimo.upper()

    return acronimo


# Ejemplo de uso
cadena = "Universidad Tecnológica Nacional Facultad Regional Avellaneda"
acrónimo = generar_acronimo(cadena)
print(acrónimo)  # Debería imprimir "UTNFRA"
