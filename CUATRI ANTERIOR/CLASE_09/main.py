
import json

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


def parse_json(nombre_archivo:str):
    lista= []
    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict["bzrp"]

    return lista

def generar_json(nombre_archivo:str, lista:list):
    dict_json = {}
    dict_json["bzrp"] = lista
    with open(nombre_archivo, "w") as archivo:
        json.dump(dict_json, archivo, indent=4)       

def parse_csv(nombre_archivo:str):
    lista = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            print(linea)
            lista_campos = linea.split(",")
            video = {}
            video["title"] = lista_campos[0]
            video["views"] = int(lista_campos[1])
            video["length"] = int(lista_campos[2])
            video["img_url"] = lista_campos[3]
            video["url"] = lista_campos[4]
            video["date"] = lista_campos[5]
            lista.append(video)

    return lista




def generar_csv(nombre_archivo:str, lista:list): 
    with open(nombre_archivo, "w") as archivo:
        for video in lista:
            mensaje = "{0},{1},{2},{3},{4},{5}\n"
            #FALTA REMPLAZAR COMAS y SALTOS DE LINEA
            mensaje = mensaje.format(   video["title"].replace(",","-").replace("\n","@"),
                                        video["views"].replace(",","-").replace("\n","@"),
                                        video["length"].replace(",","-").replace("\n","@"),
                                        video["img_url"].replace(",","-").replace("\n","@"),
                                        video["url"].replace(",","-").replace("\n","@"),
                                        video["date"].replace(",","-").replace("\n","@"))
            archivo.write(mensaje)




#generar_json("/home/mauro/Documentos/workspace_py/cursada_2023_1c/CLASE_08/data.json",lista_bzrp)
#lista_bzrp = parse_json("/home/mauro/Documentos/workspace_py/cursada_2023_1c/CLASE_08/data.json")
#generar_csv("/home/mauro/Documentos/workspace_py/cursada_2023_1c/CLASE_08/data.csv",lista_bzrp)

lista_bzrp = parse_csv("/home/mauro/Documentos/workspace_py/cursada_2023_1c/CLASE_08/data.csv")

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





















































