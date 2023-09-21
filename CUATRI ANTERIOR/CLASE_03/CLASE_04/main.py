from data import lista_bzrp
'''
[
    
    {
        'title': 'QUEVEDO || BZRP Music Sessions #52',
        'views': 227192970,
        'length': 204,
        'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg',
        'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',
        'date': '2022-07-06 00:00:00'
    }
]
1 - Tema mas visto
2 - Tema menos visto
3 - Tema mas largo
4 - Tema mas corto
5 - Duracion promedio de temas
6 - Promedio de vistas 
7 - Salir
'''

def mostrar_lista_videos ():
    for video in lista_bzrp:
        print("\nTitulo: {0}- views: {1} - length: {2}".format(video['title'],video['views'],video['length']))
            
def calcular_tema_mas_visto():
    for indice in range(len(lista_bzrp)):
        if(indice == 0 or maximo_views < lista_bzrp[indice]['views']):
            maximo_views = lista_bzrp[indice]['views']
            maximo_indice = indice
    
    print("\nTitulo: {0}- views: {1} - length: {2}".format(
                                    lista_bzrp[maximo_indice]['title'],
                                    lista_bzrp[maximo_indice]['views'],
                                    lista_bzrp[maximo_indice]['length']))
        
def calcular_tema_menos_visto():
    for indice in range(len(lista_bzrp)):
        if (indice == 0 or lista_bzrp[minimo_indice]['views'] > lista_bzrp[indice]['views']):
            minimo_indice = indice

    print("\nTitulo: {0}- views: {1} - length: {2}".format(
        lista_bzrp[minimo_indice]['title'],
        lista_bzrp[minimo_indice]['views'],
        lista_bzrp[minimo_indice]['length']))

def calcular_tema_mas_largo(): 
    for indice in range(len(lista_bzrp)):
        if(indice == 0 or lista_bzrp[maximo_indice]['length'] < lista_bzrp[indice]['length']):
            maximo_indice = indice

    print("\nTitulo: {0}- views: {1} - length: {2}".format(
                                    lista_bzrp[maximo_indice]['title'],
                                    lista_bzrp[maximo_indice]['views'],
                                    lista_bzrp[maximo_indice]['length']))

def calcular_tema_mas_corto():
    for indice in range(len(lista_bzrp)):
        if (indice == 0 or lista_bzrp[minimo_indice]['length'] > lista_bzrp[indice]['length']):
            minimo_indice = indice

    print("\nTitulo: {0}- views: {1} - length: {2}".format(
        lista_bzrp[minimo_indice]['title'],
        lista_bzrp[minimo_indice]['views'],
        lista_bzrp[minimo_indice]['length']))

def calcular_duracion_promedio():
    acumulador_duracion = 0 
    for video in lista_bzrp:
        acumulador_duracion += video['length']

    duracion_promedio = acumulador_duracion / len(lista_bzrp)
    print("La duracion promedio es: {0}".format(duracion_promedio))

def calcular_vistas_promedio():
    acumulador_vistas = 0 
    for video in lista_bzrp:
        acumulador_vistas += video['views']

    duracion_promedio = acumulador_vistas / len(lista_bzrp)
    print("Las vistas promedio son: {0}".format(duracion_promedio))

while True:
    respuesta_str = input("\n\n1 - Tema mas visto\n2 - Tema menos visto\n3 - Tema mas largo\n4 - Tema mas corto\n5 - Duracion promedio de temas\n6 - Promedio de vistas \n7 - Mostrar Lista\n8 - Salir\n\n")
    #FALTA VALIDAR
    respuesta_int = int(respuesta_str)
    match(respuesta_int):
        case 1:
            calcular_tema_mas_visto()
        case 2:
            calcular_tema_menos_visto()
        case 3:
            calcular_tema_mas_largo()
        case 4:
            calcular_tema_mas_corto()
        case 5:
            calcular_duracion_promedio()
        case 6:
            calcular_vistas_promedio()
        case 7:
            mostrar_lista_videos()
        case 8:
            break
        case _:
            print("Opcion no valida")
        
    input("\nPulse enter para continuar\n")





















































