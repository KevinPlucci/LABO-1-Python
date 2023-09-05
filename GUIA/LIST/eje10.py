# Crea una lista de palabras y muestra las palabras que tienen más de 5 letras.

# Crear una lista de palabras
palabras = ["manzana", "perro", "gato", "elefante", "computadora", "sol", "montaña"]

# Mostrar las palabras que tienen más de 5 letras
for palabra in palabras:
    if len(palabra) > 5:
        print(palabra)
