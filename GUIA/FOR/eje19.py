# Dada una lista de palabras, imprimir las palabras que tienen una letra mayúscula.

# Lista de palabras
palabras = ["Hola", "mundo", "Python", "Programación", "es", "Genial"]

# Imprimir las palabras que contienen al menos una letra mayúscula
print("Palabras que contienen al menos una letra mayúscula:")

for palabra in palabras:
    if any(letra.isupper() for letra in palabra):
        print(palabra)
