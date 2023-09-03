# Dada una lista de palabras, imprimir las palabras que tienen una letra específica.

# Lista de palabras
palabras = ["manzana", "banana", "pera", "uva", "ciruela"]

# Letra específica que deseas buscar
letra = "e"

# Imprimir las palabras que contienen la letra específica
print(f"Palabras que contienen la letra '{letra}':")

for palabra in palabras:
    if letra in palabra:
        print(palabra)
