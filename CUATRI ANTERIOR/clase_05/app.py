'''
21.Crear una función que reciba como parámetro un string y devuelva un
diccionario donde cada clave es una palabra y cada valor es un entero que
indica cuántas veces aparece esa palabra dentro del string
'''



def limpia_texto(texto:str):
    texto = texto.replace(",","")
    texto = texto.replace(":","")
    texto = texto.replace(";","")
    texto = texto.replace(".","")
    return texto

def cuenta_palabras(texto:str):
    dic_contador = {}
    lista_palabras = texto.split(" ")
    for palabra in lista_palabras:
        if palabra in dic_contador:
            dic_contador[palabra] = dic_contador[palabra] + 1
        else:
            dic_contador[palabra] = 1
    return dic_contador



print(limpia_texto("diccionario donde cada, clave es una palabra; y cada: valor es. un entero que"))


#---------------------------------------------------------------------------------------------------


# EJ 12
def validar_tarjeta(texto):
    lista = texto.split(" ")
    flag_tarjeta_ok = True
    var_texto = "ERROR"

    for e in lista:
        if(e.isdigit() == False):
            flag_tarjeta_ok = False
            break

    if(flag_tarjeta_ok and len(lista) == 4):
        var_texto = "**** {0} {1} ****".format(lista[1],lista[2])
    return var_texto


print(validar_tarjeta("1111 8888 9999 0000"))
print(validar_tarjeta("1A21 8888 9999 0000"))

#---------------------------------------------------------------------------------------------------
'''
Escribir una función que tome una lista de palabras y devuelva un string que contenga 
todas las palabras concatenadas con comas y "y" antes de la última palabra. Por ejemplo, 
si la lista es ["manzanas", "naranjas", "bananas"], el string resultante debería ser 
"manzanas, naranjas y bananas"
'''

def concatenar(palabras:list)->str:
    '''
    DOCUMENTAR
    ''' 
    texto = ""
    if(len(palabras)>1):
        for palabra in palabras[0:-1]:
            texto = "{0}{1}, ".format(texto,palabra)
        
        texto = texto[0:-2]
        texto = "{0} y {1}".format(texto,palabras[-1])
    elif(len(palabras) == 1):
        texto = palabras[0]
    else:
        texto = "-------"
    return texto


# print(concatenar(["manzanas", "manzanas", "manzanas", "naranjas", "bananas"]))
# print(concatenar(["manzanas", "bananas"]))
# print(concatenar(["manzanas"]))
# print(concatenar([]))


def concatenar2(palabras:list)->str:
    '''
    DOCUMENTAR
    ''' 
    cadena = "------"
    match(len(palabras)):
        case 0:
            cadena = "===="
        case 1:
            cadena = palabras[0]
        case _:
            cadena = ", ".join(palabras[:-1]) + " y " + palabras[-1]
    return cadena

print(concatenar2(["manzanas", "manzanas", "manzanas", "naranjas", "bananas"]))
print(concatenar2(["manzanas", "bananas"]))
print(concatenar2(["manzanas"]))
print(concatenar2([]))































