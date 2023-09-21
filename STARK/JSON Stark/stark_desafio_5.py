# stark_desafio_5.py

import json
import re


def cargar_datos():
    with open("data_stark.json", "r") as archivo_json:
        datos = json.load(archivo_json)
    return datos


def guardar_archivo(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write(contenido)
        print(f"Se creó el archivo: {nombre_archivo}")
        return True
    except Exception as e:
        print(f"Error al crear el archivo: {nombre_archivo}")
        return False


def capitalizar_palabras(texto):
    palabras = texto.split()
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
    return " ".join(palabras_capitalizadas)


def obtener_nombre_capitalizado(heroe):
    nombre = heroe.get("nombre", "N/A")
    return f"Nombre: {capitalizar_palabras(nombre)}"


def imprimir_dato(dato):
    print(dato)


def obtener_nombre_y_dato(heroe, key):
    nombre = heroe.get("nombre", "N/A")
    valor = heroe.get(key, "N/A")
    return f"Nombre: {capitalizar_palabras(nombre)} | {capitalizar_palabras(key)}: {capitalizar_palabras(valor)}"


def es_genero(heroe, genero):
    return heroe.get("genero") == genero


def stark_guardar_heroe_genero(lista_heroes, genero):
    """
    Imprime y guarda en un archivo los héroes que coinciden con el género especificado.

    :param lista_heroes: Una lista de diccionarios que contiene los datos de los superhéroes.
    :param genero: El género a evaluar (puede ser M o F).
    :return: True si pudo guardar el archivo, False en caso contrario.
    """
    genero = genero.upper()
    genero_valido = ["M", "F", "NB"]

    if genero not in genero_valido:
        print("Género no válido. Debe ser M, F o NB.")
        return False

    heroes_genero = [heroe for heroe in lista_heroes if es_genero(heroe, genero)]

    if not heroes_genero:
        print(f"No se encontraron héroes de género {genero}.")
        return False

    for heroe in heroes_genero:
        imprimir_dato(obtener_nombre_capitalizado(heroe))

    nombre_archivo = f"heroes_{genero}.csv"
    contenido = "\n".join([heroe["nombre"] for heroe in heroes_genero])

    if guardar_archivo(nombre_archivo, contenido):
        return True
    else:
        return False


def calcular_min(lista_heroes, key):
    min_heroe = lista_heroes[0]
    min_valor = min_heroe.get(key, 0)

    for heroe in lista_heroes:
        valor = heroe.get(key, 0)
        if valor < min_valor:
            min_heroe = heroe
            min_valor = valor

    return min_heroe


def calcular_max(lista_heroes, key):
    max_heroe = lista_heroes[0]
    max_valor = max_heroe.get(key, 0)

    for heroe in lista_heroes:
        valor = heroe.get(key, 0)
        if valor > max_valor:
            max_heroe = heroe
            max_valor = valor

    return max_heroe


def calcular_max_min_dato(lista_heroes, key, tipo_calculo):
    """
    Calcula y devuelve el héroe con el valor máximo o mínimo de la clave especificada.

    :param lista_heroes: Una lista de diccionarios que contiene los datos de los superhéroes.
    :param key: La clave (por ejemplo, "altura", "fuerza") para calcular el máximo o mínimo.
    :param tipo_calculo: El tipo de cálculo a realizar, puede ser "maximo" o "minimo".
    :return: Un diccionario que representa al héroe con el valor máximo o mínimo de la clave especificada.
    """
    if tipo_calculo == "maximo":
        return calcular_max(lista_heroes, key)
    elif tipo_calculo == "minimo":
        return calcular_min(lista_heroes, key)
    else:
        print("Tipo de cálculo no válido. Debe ser 'maximo' o 'minimo'.")
        return None


def calcular_promedio(lista_heroes, key):
    total = 0
    cantidad = len(lista_heroes)

    for heroe in lista_heroes:
        total += heroe.get(key, 0)

    if cantidad > 0:
        promedio = total / cantidad
        return promedio
    else:
        return None


def stark_calcular_imprimir_heroe(lista_heroes, key):
    """
    Calcula, imprime y guarda en un archivo el héroe con el valor máximo o mínimo de la clave especificada.

    :param lista_heroes: Una lista de diccionarios que contiene los datos de los superhéroes.
    :param key: La clave (por ejemplo, "altura", "fuerza") para calcular el máximo o mínimo.
    """
    tipo_calculo = input(
        f"¿Desea calcular el máximo o el mínimo para {key}? (maximo/minimo): "
    ).lower()

    heroe_calculado = calcular_max_min_dato(lista_heroes, key, tipo_calculo)

    if heroe_calculado:
        imprimir_dato(obtener_nombre_y_dato(heroe_calculado, key))

        nombre_archivo = f"heroes_{tipo_calculo}_{key}.csv"
        contenido = f"{key.capitalize()}: {heroe_calculado[key]}"

        if guardar_archivo(nombre_archivo, contenido):
            print(f"Se creó el archivo: {nombre_archivo}")
        else:
            print(f"Error al crear el archivo: {nombre_archivo}")


def calcular_promedio_genero(lista_heroes, key, genero):
    """
    Calcula el promedio de un atributo (key) para héroes de un género específico.

    :param lista_heroes: Lista de héroes en forma de diccionarios.
    :param key: La clave (atributo) para el cual se calculará el promedio.
    :param genero: El género de los héroes a considerar (M o F).
    :return: El promedio del atributo para el género especificado.
    """
    suma = 0
    cantidad = 0

    for heroe in lista_heroes:
        if heroe.get("genero") == genero:
            valor = heroe.get(key)
            if valor is not None and valor != "":
                suma += float(valor)
                cantidad += 1

    if cantidad == 0:
        return 0  # Evitar la división por cero
    else:
        return suma / cantidad


# Modificar la función stark_calcular_imprimir_guardar_promedio_altura_genero para imprimir en lugar de guardar en CSV
def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes, genero):
    altura_promedio = calcular_promedio_genero(lista_heroes, "altura", genero)
    if genero == "M":
        print(
            f"Altura promedio de los superhéroes de género M: {altura_promedio:.2f} cm"
        )
    elif genero == "F":
        print(
            f"Altura promedio de las superhéroes de género F: {altura_promedio:.2f} cm"
        )


def stark_imprimir_superheroes_genero_M(lista_heroes):
    """
    Imprime por consola el nombre de cada superhéroe de género M.

    :param lista_heroes: Una lista de diccionarios que contiene los datos de los superhéroes.
    """
    for heroe in lista_heroes:
        if heroe.get("genero") == "M":
            print(obtener_nombre_capitalizado(heroe))


def stark_imprimir_superheroes_genero_F(lista_heroes):
    """
    Imprime por consola el nombre de cada superhéroe de género F.

    :param lista_heroes: Una lista de diccionarios que contiene los datos de los superhéroes.
    """
    for heroe in lista_heroes:
        if heroe.get("genero") == "F":
            print(obtener_nombre_capitalizado(heroe))


def stark_calcular_imprimir_heroe_mas_alto_genero_M(lista_heroes):
    """
    Calcula e imprime al superhéroe más alto de género M.

    :param lista_heroes: Una lista de diccionarios que contiene los datos de los superhéroes.
    """
    heroe_mas_alto = None

    for heroe in lista_heroes:
        if heroe.get("genero") == "M":
            if heroe_mas_alto is None or heroe.get("altura", 0) > heroe_mas_alto.get(
                "altura", 0
            ):
                heroe_mas_alto = heroe

    if heroe_mas_alto:
        imprimir_dato(
            f"Superhéroe más alto de género M: {obtener_nombre_y_dato(heroe_mas_alto, 'altura')}"
        )
    else:
        print("No se encontraron superhéroes de género M.")


def stark_calcular_imprimir_heroe_mas_alto_genero_F(lista_heroes):
    """
    Calcula e imprime al superhéroe más alto de género F.

    :param lista_heroes: Una lista de diccionarios que contiene los datos de los superhéroes.
    """
    heroe_mas_alto_genero_F = None

    for heroe in lista_heroes:
        if heroe.get("genero") == "F":
            if heroe_mas_alto_genero_F is None or heroe.get(
                "altura", 0
            ) > heroe_mas_alto_genero_F.get("altura", 0):
                heroe_mas_alto_genero_F = heroe

    if heroe_mas_alto_genero_F:
        imprimir_dato(
            f"Superhéroe más alto de género F: {obtener_nombre_y_dato(heroe_mas_alto_genero_F, 'altura')}"
        )
    else:
        print("No se encontraron superhéroes de género F.")


def stark_calcular_imprimir_heroe_mas_bajo_genero_M(lista_heroes):
    """
    Calcula e imprime al superhéroe más bajo de género M.

    :param lista_heroes: Una lista de diccionarios que contiene los datos de los superhéroes.
    """
    heroe_mas_bajo_genero_M = None

    for heroe in lista_heroes:
        if heroe.get("genero") == "M":
            if heroe_mas_bajo_genero_M is None or heroe.get(
                "altura", float("inf")
            ) < heroe_mas_bajo_genero_M.get("altura", float("inf")):
                heroe_mas_bajo_genero_M = heroe

    if heroe_mas_bajo_genero_M:
        imprimir_dato(
            f"Superhéroe más bajo de género M: {obtener_nombre_y_dato(heroe_mas_bajo_genero_M, 'altura')}"
        )
    else:
        print("No se encontraron superhéroes de género M.")


def stark_calcular_imprimir_heroe_mas_bajo_genero_F(lista_heroes):
    """
    Calcula e imprime al superhéroe más bajo de género F.

    :param lista_heroes: Una lista de diccionarios que contiene los datos de los superhéroes.
    """
    heroe_mas_bajo_genero_F = None

    for heroe in lista_heroes:
        if heroe.get("genero") == "F":
            if heroe_mas_bajo_genero_F is None or heroe.get(
                "altura", float("inf")
            ) < heroe_mas_bajo_genero_F.get("altura", float("inf")):
                heroe_mas_bajo_genero_F = heroe

    if heroe_mas_bajo_genero_F:
        imprimir_dato(
            f"Superhéroe más bajo de género F: {obtener_nombre_y_dato(heroe_mas_bajo_genero_F, 'altura')}"
        )
    else:
        print("No se encontraron superhéroes de género F.")


def guardar_promedio_altura_genero(altura_promedio, genero):
    """
    Guarda el promedio de altura de los héroes de un género en un archivo CSV.

    :param altura_promedio: El promedio de altura a guardar.
    :param genero: El género de los héroes a calcular (M o F).
    :return: True si pudo guardar el archivo, False en caso contrario.
    """
    nombre_archivo = f"heroes_promedio_altura_{genero}.csv"
    contenido = f"Altura promedio género {genero}: {altura_promedio:.2f}\n"

    return guardar_archivo(nombre_archivo, contenido)


def calcular_cantidad_tipo(lista_heroes, tipo_dato):
    """
    Calcula la cantidad de héroes para cada variedad del tipo de dato especificado.

    :param lista_heroes: Una lista de diccionarios que contiene los datos de los superhéroes.
    :param tipo_dato: El tipo de dato/key a buscar (color_ojos, color_pelo, etc).
    :return: Un diccionario con la cantidad de cada variedad del tipo de dato.
    """
    cantidad_tipo = {}

    for heroe in lista_heroes:
        valor = heroe.get(tipo_dato, "N/A")
        valor = capitalizar_palabras(valor)
        if valor in cantidad_tipo:
            cantidad_tipo[valor] += 1
        else:
            cantidad_tipo[valor] = 1

    return cantidad_tipo


def guardar_cantidad_heroes_tipo(cantidad_tipo, tipo_dato):
    """
    Guarda la cantidad de héroes por tipo de dato en un archivo CSV.

    :param cantidad_tipo: Un diccionario con la cantidad de héroes por tipo de dato.
    :param tipo_dato: El tipo de dato a evaluar (color_pelo, color_ojos, etc).
    :return: True si pudo guardar el archivo, False en caso contrario.
    """
    nombre_archivo = f"heroes_cantidad_{tipo_dato}.csv"
    contenido = ""

    for tipo, cantidad in cantidad_tipo.items():
        contenido += f"Caracteristica: {tipo} - Cantidad de heroes: {cantidad}\n"

    return guardar_archivo(nombre_archivo, contenido)


def stark_calcular_cantidad_por_tipo(lista_heroes, tipo_dato):
    """
    Calcula, imprime y guarda en un archivo la cantidad de héroes por tipo de dato.

    :param lista_heroes: Una lista de diccionarios que contiene los datos de los superhéroes.
    :param tipo_dato: El tipo de dato a evaluar (color_pelo, color_ojos, etc).
    """
    cantidad_tipo = calcular_cantidad_tipo(lista_heroes, tipo_dato)

    if not cantidad_tipo:
        print("La lista de héroes está vacía.")
        return False

    for tipo, cantidad in cantidad_tipo.items():
        imprimir_dato(f"Caracteristica: {tipo} - Cantidad de heroes: {cantidad}")

    if guardar_cantidad_heroes_tipo(cantidad_tipo, tipo_dato):
        return True
    else:
        return False


def obtener_lista_de_tipos(lista_heroes, tipo_dato):
    """
    Obtiene una lista de las variedades del tipo de dato especificado.

    :param lista_heroes: Una lista de diccionarios que contiene los datos de los superhéroes.
    :param tipo_dato: El tipo de dato/key a buscar (color_ojos, color_pelo, etc).
    :return: Un set con las variedades del tipo de dato.
    """
    tipos = set()

    for heroe in lista_heroes:
        valor = heroe.get(tipo_dato, "N/A")
        valor = capitalizar_palabras(valor)
        tipos.add(valor)

    return tipos


def normalizar_dato(dato, valor_default="N/A"):
    """
    Normaliza un dato, reemplazando un valor vacío por un valor predeterminado.

    :param dato: El dato a normalizar.
    :param valor_default: El valor por defecto a colocar en caso de que el dato esté vacío.
    :return: El dato normalizado.
    """
    if not dato:
        return valor_default
    else:
        return dato


def normalizar_heroe(heroe, key):
    """
    Normaliza un héroe, capitalizando las palabras de la clave especificada y normalizando su valor.

    :param heroe: Un diccionario que representa al héroe.
    :param key: La clave que se debe normalizar.
    :return: El héroe con la clave normalizada y el valor normalizado.
    """
    heroe_normalizado = heroe.copy()
    heroe_normalizado[key] = normalizar_dato(heroe.get(key))
    return heroe_normalizado


def obtener_heroes_por_tipo(lista_heroes, tipos, tipo_dato):
    """
    Obtiene los héroes que coinciden con los tipos de dato especificados.

    :param lista_heroes: Una lista de diccionarios que contiene los datos de los superhéroes.
    :param tipos: Un set de tipos/variedades (colores de ojos, de pelo, etc).
    :param tipo_dato: El tipo de dato a evaluar (la key en cuestion, color_ojos, color_pelo, etc).
    :return: Un diccionario con cada variedad como key y una lista de nombres de héroes como valor.
    """
    heroes_por_tipo = {tipo: [] for tipo in tipos}

    for tipo in tipos:
        for heroe in lista_heroes:
            heroe_normalizado = normalizar_heroe(heroe, tipo_dato)
            valor = heroe_normalizado.get(tipo_dato, "N/A")

            if valor == tipo:
                heroes_por_tipo[tipo].append(heroe_normalizado["nombre"])

    return heroes_por_tipo


def guardar_heroes_por_tipo(heroes_por_tipo, tipo_dato):
    """
    Guarda los héroes agrupados por tipo de dato en un archivo CSV.

    :param heroes_por_tipo: Un diccionario con los héroes agrupados por tipo de dato.
    :param tipo_dato: El tipo de dato a evaluar (color_pelo, color_ojos, etc).
    :return: True si pudo guardar el archivo, False en caso contrario.
    """
    nombre_archivo = f"heroes_segun_{tipo_dato}.csv"
    contenido = ""

    for tipo, heroes in heroes_por_tipo.items():
        heroes_str = " | ".join(heroes)
        contenido += f"{tipo.capitalize()}: {heroes_str}\n"

    return guardar_archivo(nombre_archivo, contenido)


def stark_listar_heroes_por_dato(lista_heroes, tipo_dato):
    """
    Lista, imprime y guarda en un archivo los héroes agrupados por tipo de dato.

    :param lista_heroes: Una lista de diccionarios que contiene los datos de los superhéroes.
    :param tipo_dato: El tipo de dato a evaluar (color_pelo, color_ojos, etc).
    """
    tipos = obtener_lista_de_tipos(lista_heroes, tipo_dato)

    if not tipos:
        print("No se encontraron tipos de dato.")
        return False

    heroes_por_tipo = obtener_heroes_por_tipo(lista_heroes, tipos, tipo_dato)

    for tipo, heroes in heroes_por_tipo.items():
        imprimir_dato(f"{tipo.capitalize()}: {', '.join(heroes)}")

    if guardar_heroes_por_tipo(heroes_por_tipo, tipo_dato):
        return True
    else:
        return False


def imprimir_menu_desafio_5():
    print("Menú Desafío #05:")
    print(
        "A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M"
    )
    print(
        "B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F"
    )
    print(
        "C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M"
    )
    print(
        "D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F"
    )
    print(
        "E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M"
    )
    print(
        "F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F"
    )
    print(
        "G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M"
    )
    print(
        "H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F"
    )
    print(
        "I. Calcular y guardar en un archivo CSV la cantidad de héroes de cada color de ojos"
    )
    print(
        "J. Calcular y guardar en un archivo CSV la cantidad de héroes de cada color de pelo"
    )
    print(
        "K. Listar y guardar en un archivo CSV los héroes agrupados por color de ojos"
    )
    print(
        "L. Listar y guardar en un archivo CSV los héroes agrupados por color de pelo"
    )
    print("X. Salir")


# Modificar el menú para quitar la opción de guardar en CSV
def main():
    datos = cargar_datos()
    lista_heroes = datos.get("heroes", [])

    if not lista_heroes:
        print("No se encontraron datos de superhéroes.")
        return

    while True:
        imprimir_menu_desafio_5()
        opcion = input("Seleccione una opción (A/B/C/D/E/F/G/H/I/J/K/L/X): ").upper()

        if opcion == "A":
            stark_imprimir_superheroes_genero_M(lista_heroes)
        elif opcion == "B":
            stark_imprimir_superheroes_genero_F(lista_heroes)
        elif opcion == "C":
            stark_calcular_imprimir_heroe_mas_alto_genero_M(lista_heroes)
        elif opcion == "D":
            stark_calcular_imprimir_heroe_mas_alto_genero_F(lista_heroes)
        elif opcion == "E":
            stark_calcular_imprimir_heroe_mas_bajo_genero_M(lista_heroes)
        elif opcion == "F":
            stark_calcular_imprimir_heroe_mas_bajo_genero_F(lista_heroes)
        elif opcion == "G":
            stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes, "M")
        elif opcion == "H":
            stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes, "F")
        elif opcion == "I":
            stark_calcular_cantidad_por_tipo(lista_heroes, "color_ojos")
        elif opcion == "J":
            stark_calcular_cantidad_por_tipo(lista_heroes, "color_pelo")
        elif opcion == "K":
            stark_listar_heroes_por_dato(lista_heroes, "color_ojos")
        elif opcion == "L":
            stark_listar_heroes_por_dato(lista_heroes, "color_pelo")
        elif opcion == "X":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
