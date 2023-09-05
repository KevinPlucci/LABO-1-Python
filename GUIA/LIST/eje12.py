# Crea una lista con los nombres de tus 3 películas favoritas y luego imprime los elementos en orden inverso (sin utilizar el método reverse())

# Crear una lista con los nombres de tus 3 películas favoritas
peliculas_favoritas = ["Película 1", "Película 2", "Película 3"]

# Imprimir los elementos en orden inverso
for i in range(len(peliculas_favoritas) - 1, -1, -1):
    print(peliculas_favoritas[i])
