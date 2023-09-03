# Dada una lista de palabras, imprimir las palabras que comienzan y terminan con la misma letra.

# Lista de palabras
palabras = ["anilina", "oso", "casa", "manzana", "python", "nivel"]

# Iterar a través de la lista de palabras
for palabra in palabras:
    # Verificar si la primera y última letra son iguales (ignorar mayúsculas/minúsculas)
    if palabra[0].lower() == palabra[-1].lower():
        print(palabra)
