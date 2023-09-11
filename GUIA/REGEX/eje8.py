# Crear una función que reciba una lista de palabras y devuelva otra lista con las palabras  que comienzan con la letra ‘U’


def palabras_con_U(lista_palabras):
    # Utilizamos una comprensión de lista para filtrar las palabras que comienzan con 'U'
    palabras_con_U = [palabra for palabra in lista_palabras if palabra.startswith("U")]
    return palabras_con_U


# Ejemplo de uso:
lista_palabras = ["Uno", "Uva", "Manzana", "Universo", "Perro"]
resultado = palabras_con_U(lista_palabras)
print(resultado)  # Debería devolver ['Uno', 'Uva', 'Universo']
