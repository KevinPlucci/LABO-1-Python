# Dada una lista de palabras, imprimir la cantidad total de vocales en la lista.

# Lista de palabras
palabras = ["hola", "mundo", "Python", "programación"]

# Inicializar la cantidad total de vocales
total_vocales = 0

# Iterar a través de las palabras en la lista y contar las vocales
for palabra in palabras:
    for letra in palabra:
        if letra.lower() in "aeiouáéíóú":
            total_vocales += 1  # Usamos letra.lower() para considerar tanto vocales mayúsculas como minúsculas

# Imprimir la cantidad total de vocales
print("La cantidad total de vocales en la lista de palabras es:", total_vocales)
