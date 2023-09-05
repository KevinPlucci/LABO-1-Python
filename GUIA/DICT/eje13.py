# Crea un diccionario que contenga el nombre y el nivel de dificultad de varios juegos de mesa.
# Luego, pedirle al usuario un nivel de dificultad, buscar los que coinciden e imprimir sus nombres

# Crear un diccionario con juegos de mesa y sus niveles de dificultad
juegos_de_mesa = {
    "Ajedrez": "Alto",
    "Catan": "Medio",
    "Dominó": "Bajo",
    "Risk": "Alto",
    "Scrabble": "Medio",
    "Monopoly": "Bajo",
}

# Pedir al usuario que ingrese un nivel de dificultad
nivel_buscado = input("Ingrese un nivel de dificultad (Alto, Medio o Bajo): ")

# Inicializar una lista para almacenar los juegos que coinciden con el nivel
juegos_coincidentes = []

# Buscar juegos que coincidan con el nivel ingresado por el usuario
for juego, nivel in juegos_de_mesa.items():
    if nivel.lower() == nivel_buscado.lower():
        juegos_coincidentes.append(juego)

# Imprimir los juegos que coinciden con el nivel
if juegos_coincidentes:
    print("Juegos de nivel '{}':".format(nivel_buscado))
    for juego in juegos_coincidentes:
        print(juego)
else:
    print("No se encontraron juegos con el nivel '{}'.".format(nivel_buscado))
