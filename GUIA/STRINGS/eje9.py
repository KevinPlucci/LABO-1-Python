# Escribir una función que tome una lista de nombres y los una en una sola cadena separada por un salto de línea, por ejemplo: ["Juan", "María", "Pedro"] -> "Juan\nMaría\nPedro".


def unir_nombres_con_salto_de_linea(nombres):
    # Usar el método join para unir los nombres con saltos de línea
    nombres_unidos = "\n".join(nombres)

    return nombres_unidos


# Ejemplo de uso
lista_de_nombres = ["Juan", "María", "Pedro"]
resultado = unir_nombres_con_salto_de_linea(lista_de_nombres)
print(resultado)
