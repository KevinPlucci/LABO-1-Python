# Crea un diccionario que contenga las capitales de los países de América del Sur. Luego, pide al usuario que ingrese el nombre de un país y muestra su capital correspondiente.

# Crear el diccionario de capitales de América del Sur
capitales_americadel_sur = {
    "Argentina": "Buenos Aires",
    "Bolivia": "La Paz",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "Ecuador": "Quito",
    "Guyana": "Georgetown",
    "Paraguay": "Asunción",
    "Perú": "Lima",
    "Surinam": "Paramaribo",
    "Uruguay": "Montevideo",
    "Venezuela": "Caracas",
}

# Pedir al usuario que ingrese un país
pais = input("Ingresa el nombre de un país de América del Sur: ")

# Obtener la capital correspondiente al país ingresado (si existe)
capital = capitales_americadel_sur.get(pais)

# Verificar si el país existe en el diccionario
if capital:
    print(f"La capital de {pais} es {capital}.")
else:
    print(f"No se encontró información sobre la capital de {pais}.")
