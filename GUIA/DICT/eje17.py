# Crea un diccionario que represente las películas de un cine, donde las claves son los nombres de las películas y los valores son los horarios correspondientes.
# Modifica el horario de la película "Avengers: Endgame" a las 19:30.

# Crear un diccionario con las películas y sus horarios
peliculas_cine = {
    "Spider-Man: No Way Home": "15:00",
    "The Matrix Resurrections": "17:30",
    "Dune": "20:00",
    "Avengers: Endgame": "18:45",  # Horario original
    "Joker": "22:15",
}

# Mostrar la lista de películas y sus horarios
print("Lista de películas y sus horarios:")
for pelicula, horario in peliculas_cine.items():
    print("{}: {}".format(pelicula, horario))

# Modificar el horario de la película "Avengers: Endgame"
nuevo_horario = "19:30"
peliculas_cine["Avengers: Endgame"] = nuevo_horario

# Mostrar la lista actualizada de películas y sus horarios
print("\nLista de películas y sus horarios actualizada:")
for pelicula, horario in peliculas_cine.items():
    print("{}: {}".format(pelicula, horario))
