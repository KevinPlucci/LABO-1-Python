# Dada una lista de palabras, imprimir las palabras que tienen una longitud impar.

# Lista de palabras
palabras = ["hola", "mundo", "Python", "programación", "corta", "larga"]

# Imprimir las palabras con longitud impar
print("Palabras con longitud impar:")

for palabra in palabras:
    if len(palabra) % 2 != 0:
        print(palabra)
