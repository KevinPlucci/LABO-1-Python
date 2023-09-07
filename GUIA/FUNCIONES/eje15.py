# Crear una función que recibe una lista de diccionarios con información de películas (título, género, director) y devuelve un diccionario con la cantidad de películas por género.


def contar_peliculas_por_genero(lista_peliculas):
    # Creamos un diccionario para almacenar la cantidad de películas por género
    generos = {}

    # Recorremos la lista de películas y contamos por género
    for pelicula in lista_peliculas:
        genero = pelicula.get("genero")
        if genero in generos:
            generos[genero] += 1
        else:
            generos[genero] = 1

    return generos


# Ejemplo de uso
peliculas = [
    {"titulo": "Pelicula1", "genero": "Acción", "director": "Director1"},
    {"titulo": "Pelicula2", "genero": "Drama", "director": "Director2"},
    {"titulo": "Pelicula3", "genero": "Acción", "director": "Director3"},
    {"titulo": "Pelicula4", "genero": "Comedia", "director": "Director4"},
    {"titulo": "Pelicula5", "genero": "Drama", "director": "Director5"},
]

resultado = contar_peliculas_por_genero(peliculas)
print(resultado)
