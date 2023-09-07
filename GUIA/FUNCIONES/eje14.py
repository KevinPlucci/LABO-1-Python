# Crear una función que recibe una lista de números y devuelve un diccionario con el valor mínimo, el valor máximo y el promedio de los números en la lista.


def estadisticas_lista_numeros(lista_numeros):
    if not lista_numeros:
        return None  # Si la lista está vacía, retornamos None

    # Calculamos el valor mínimo, máximo y promedio
    valor_minimo = min(lista_numeros)
    valor_maximo = max(lista_numeros)
    promedio = sum(lista_numeros) / len(lista_numeros)

    # Creamos un diccionario con las estadísticas
    estadisticas = {
        "minimo": valor_minimo,
        "maximo": valor_maximo,
        "promedio": promedio,
    }

    return estadisticas


# Ejemplo de uso
numeros = [10, 20, 5, 15, 30]
resultado = estadisticas_lista_numeros(numeros)
print(resultado)
