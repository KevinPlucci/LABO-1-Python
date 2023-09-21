
'''
    Acción.
    Aventuras.
    Ciencia Ficción.
    Comedia.
    Documental
    Drama
    Fantasía
    Musical

[
    
    {
        'titulo': 'Volver al Futuro',
        'genero': ̈́'Ciencia Ficción',
        'director': 'Robert Zemeckis'
    },
    {
        'titulo': 'Volver al Futuro II',
        'genero': ̈́'Ciencia Ficción',
        'director': 'Robert Zemeckis'
    },
    {
        'titulo': 'Volver al Futuro III',
        'genero': ̈́'Ciencia Ficción',
        'director': 'Robert Zemeckis'
    },
    {
        'titulo': 'Volver al Futuro III',
        'genero': ̈́'Ciencia Ficción',
        'director': 'Robert Zemeckis'
    }
]

Crear una función que recibe una lista de diccionarios con información de películas 
(título, género, director) y devuelve un diccionario con la cantidad de películas 
por género.

'''



lista_pelis = [
    {
        'titulo': 'Volver al Futuro',
        'genero': 'Ciencia Ficción',
        'director': 'Robert Zemeckis'
    },
    {
        'titulo': 'Volver al Futuro II',
        'genero': 'Ciencia Ficción',
        'director': 'Robert Zemeckis'
    },
    {
        'titulo': 'Volver al Futuro III',
        'genero': 'Ciencia Ficción',
        'director': 'Robert Zemeckis'
    },
    {
        'titulo': 'El padrino I',
        'genero': 'Drama',
        'director': 'Francis Ford Coppola'
    },
    {
        'titulo': 'El padrino II',
        'genero': 'Drama',
        'director': 'Francis Ford Coppola'
    }
]



def calcular_peliculas_por_genero2(lista_de_peliculas):

    dic_contador_generos  = {} # {'Ciencia Ficción': 3, 'Drama': 2}
    
    for pelicula in lista_de_peliculas:
        texto_genero = pelicula['genero']

        if texto_genero in dic_contador_generos:
            dic_contador_generos[texto_genero] += 1
        else:
            dic_contador_generos[texto_genero] = 1

    return dic_contador_generos



def calcular_peliculas_por_genero(lista_de_peliculas):

    dic_contador_generos  = {} 


    
    
    for pelicula in lista_de_peliculas:
        texto_genero = pelicula['genero']
        texto_titulo = pelicula['titulo']
                
        if texto_genero in dic_contador_generos:
            auxiliar_lista = []
            auxiliar_lista = dic_contador_generos[texto_genero]
            auxiliar_lista.append(texto_titulo)
            #dic_contador_generos[texto_genero].append(texto_titulo)
        else:
            auxiliar_lista = []
            auxiliar_lista.append(texto_titulo)
            dic_contador_generos[texto_genero] = auxiliar_lista

    return dic_contador_generos





dic_resultado = calcular_peliculas_por_genero(lista_pelis)

for genero in dic_resultado:
    print("------------------")
    print(genero)
    print(len(dic_resultado[genero]))
    print(dic_resultado[genero])















































