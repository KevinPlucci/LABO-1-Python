# Crea una función que reciba dos listas de nombres, y devuelva una lista con los nombres que aparecen en ambas listas


def nombres_en_comun(lista1, lista2):
    # Convertimos ambas listas en conjuntos (sets) para facilitar la operación de intersección
    set_lista1 = set(lista1)
    set_lista2 = set(lista2)

    # Encontramos la intersección de los conjuntos
    nombres_comunes = set_lista1.intersection(set_lista2)

    # Convertimos el resultado de nuevo a lista
    lista_nombres_comunes = list(nombres_comunes)

    return lista_nombres_comunes


# Ejemplo de uso
nombres1 = ["Juan", "María", "Pedro", "Ana", "Luis"]
nombres2 = ["Ana", "Luis", "Elena", "Carlos"]

nombres_comunes = nombres_en_comun(nombres1, nombres2)
print(f"Nombres en común: {nombres_comunes}")
