# Crea un diccionario que represente los juegos de una consola, donde las claves son los nombres de los juegos y los valores son las puntuaciones correspondientes.
# Solicita al usuario el nombre de un juego y luego su puntuación, si el juego no existe agregarlo y si existe actualizar su puntuación

# Crear un diccionario con juegos y sus puntuaciones
juegos_consola = {
    "Mario Kart 8 Deluxe": 90,
    "The Legend of Zelda: Breath of the Wild": 95,
    "Super Smash Bros. Ultimate": 88,
    "Animal Crossing: New Horizons": 92,
}

# Mostrar la lista de juegos y sus puntuaciones
print("Lista de juegos y sus puntuaciones:")
for juego, puntuacion in juegos_consola.items():
    print("{}: {}".format(juego, puntuacion))

# Solicitar al usuario el nombre de un juego y su puntuación
nombre_juego = input("Ingrese el nombre del juego: ")
puntuacion = int(input("Ingrese la puntuación para {}: ".format(nombre_juego)))

# Verificar si el juego existe en el diccionario
if nombre_juego in juegos_consola:
    # Actualizar la puntuación del juego existente
    juegos_consola[nombre_juego] = puntuacion
    print(
        "La puntuación para {} ha sido actualizada a {}".format(
            nombre_juego, puntuacion
        )
    )
else:
    # Agregar el juego y su puntuación si no existe
    juegos_consola[nombre_juego] = puntuacion
    print(
        "{} ha sido agregado con una puntuación de {}".format(nombre_juego, puntuacion)
    )

# Mostrar la lista actualizada de juegos y sus puntuaciones
print("\nLista de juegos y sus puntuaciones actualizada:")
for juego, puntuacion in juegos_consola.items():
    print("{}: {}".format(juego, puntuacion))
