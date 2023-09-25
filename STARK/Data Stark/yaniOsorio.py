from data_stark import lista_personajes


def stark_normalizar_datos(lista_personajes):
    if not lista_personajes:
        print("Error: Lista de héroes vacía")
        return
    datos_modificados = False
    for heroe in lista_personajes:
        for key, value in heroe.items():
            if key == "edad" and not isinstance(value, int):
                heroe[key] = int(value)
                datos_modificados = True
            elif key == "altura" and not isinstance(value, float):
                heroe[key] = float(value)
                datos_modificados = True
            elif key == "fuerza" and not isinstance(value, float):
                heroe[key] = float(value)
                datos_modificados = True
    if datos_modificados:
        print("Datos normalizados")


def obtener_nombre(heroe):
    nombre = heroe["nombre"]
    return f"Nombre: {nombre}"


def imprimir_dato(texto):
    print(texto)


def stark_imprimir_nombres_heroes(lista_personajes):
    if not lista_personajes:
        return -1
    nombres = [obtener_nombre(heroe) for heroe in lista_personajes]
    return nombres


nombres_heroes = stark_imprimir_nombres_heroes(lista_personajes)
if nombres_heroes:
    for nombre in nombres_heroes:
        imprimir_dato(nombre)


def obtener_nombre_y_dato(heroe, key):
    nombre = heroe["nombre"]
    valor = heroe.get(key, "Dato no encontrado")
    return f"Nombre: {nombre} | {key}: {valor}"


altura = "altura"

for heroe in lista_personajes:
    imprimir_dato(obtener_nombre_y_dato(heroe, altura))
# obtener_nombre_y_dato(lista_personajes[0], altura)
