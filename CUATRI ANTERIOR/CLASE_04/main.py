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


def print_tema(tema):
    '''
    Mustra un tema por terminal
    Recibe el diccionario del tema a mostrar
    Retorno - No aplica
    '''    
    print("\nTitulo: {0}- views: {1} - length: {2}".format(
                                    tema['title'],
                                    tema['views'],
                                    tema['length']))

def mostrar_lista_videos (lista_de_temas):
    '''
    Muestra una lista de temas por terminal
    Recibe la lista de temas
    Retorno - No aplica
    '''    
    for tema in lista_de_temas:
        print_tema(tema)


def calcular_tema_mas_menos_por_clave(lista_de_temas,clave,maximo=True ):
    '''
    Calcula el tema mas/menos por clave ( views - length )
    Recibe la lista de temas,clave ( views - length ) y parametro que indica si busca max o min
    Retorno - El dict del tema mas/menos visto
    '''    
    indice_max_min = 0
    for indice_actual in range(1,len(lista_de_temas)):
        if(maximo):
            if(lista_de_temas[indice_actual][clave] > lista_de_temas[indice_max_min][clave]):
                indice_max_min = indice_actual
        else:
            if(lista_de_temas[indice_actual][clave] < lista_de_temas[indice_max_min][clave]):
                indice_max_min = indice_actual
            
    return lista_de_temas[indice_max_min]




    
        





def calcular_tema_menos_visto():
    pass

def calcular_tema_mas_largo(): 
    pass

def calcular_tema_mas_corto():
    pass

def calcular_duracion_promedio():
    pass

def calcular_vistas_promedio():
    pass

while True:
    respuesta_str = input("\n\n1 - Tema mas visto\n2 - Tema menos visto\n3 - Tema mas largo\n4 - Tema mas corto\n5 - Duracion promedio de temas\n6 - Promedio de vistas \n7 - Mostrar Lista\n8 - Salir\n\n")
    #FALTA VALIDAR
    respuesta_int = int(respuesta_str)
    match(respuesta_int):
        case 1:
            tema_mas_visto = calcular_tema_mas_menos_por_clave(lista_bzrp,clave= 'views')
            print_tema(tema_mas_visto)
        case 2:
            tema_menos_visto = calcular_tema_mas_menos_por_clave(lista_bzrp,clave= 'views',maximo=False)
            print_tema(tema_menos_visto)
        case 3:
            tema_mas_largo = calcular_tema_mas_menos_por_clave(lista_bzrp, clave= 'length')
            print_tema(tema_mas_largo)
        case 4:
            tema_mas_corto = calcular_tema_mas_menos_por_clave(lista_bzrp, clave= 'length',maximo=False)
            print_tema(tema_mas_corto)
        case 5:
            calcular_duracion_promedio()
        case 6:
            calcular_vistas_promedio()
        case 7:
            mostrar_lista_videos(lista_bzrp)
        case 8:
            break
        case _:
            print("Opcion no valida")
        
    input("\nPulse enter para continuar\n")





















































