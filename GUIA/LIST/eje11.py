# Crea una lista de palabras y pide al usuario que ingrese una palabra. Luego, muestra todas las palabras de la lista que tienen la misma longitud que la palabra ingresada.

# Crear una lista de palabras
palabras = ["manzana", "perro", "gato", "elefante", "computadora", "sol", "montaña"]

# Solicitar al usuario que ingrese una palabra
palabra_ingresada = input("Ingrese una palabra: ")

# Calcular la longitud de la palabra ingresada
longitud_palabra_ingresada = len(palabra_ingresada)

# Mostrar las palabras de la lista que tienen la misma longitud que la palabra ingresada
print("Palabras de la lista con la misma longitud que la palabra ingresada:")
for palabra in palabras:
    if len(palabra) == longitud_palabra_ingresada:
        print(palabra)
