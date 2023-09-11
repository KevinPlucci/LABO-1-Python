# Escribir una función que tome una lista de palabras y devuelva un string que contenga todas las palabras concatenadas con comas y "y" antes de la última palabra.
# Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"], el string resultante debería ser "manzanas, naranjas y bananas"..


def unir_palabras(lista_palabras):
    if len(lista_palabras) == 0:
        return ""
    elif len(lista_palabras) == 1:
        return lista_palabras[0]
    else:
        palabras_excepto_ultima = ", ".join(lista_palabras[:-1])
        ultima_palabra = lista_palabras[-1]
        return f"{palabras_excepto_ultima} y {ultima_palabra}"


# Ejemplo de uso
lista_palabras = ["manzanas", "naranjas", "bananas"]
resultado = unir_palabras(lista_palabras)
print(resultado)  # Esto imprimirá "manzanas, naranjas y bananas"
