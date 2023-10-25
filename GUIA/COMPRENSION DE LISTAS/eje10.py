"""
Dada una lista de nombres:
lista_nombres = ["Lourdes", "Ignacio", "Adela", "Roberto", "Marina", "Ramón", "Ezequiel", "Rodrigo", "Beatriz", "Miguel"]
Crea una lista que contenga sólo las primeras tres letras de los nombres que comienzan con una vocal 

"""

lista_nombres = [
    "Lourdes",
    "Ignacio",
    "Adela",
    "Roberto",
    "Marina",
    "Ramón",
    "Ezequiel",
    "Rodrigo",
    "Beatriz",
    "Miguel",
]

# Inicializa una lista vacía para almacenar las primeras tres letras de los nombres que cumplen con la condición.
nombres_vocales = []

# Define las vocales en una lista para verificar si un nombre comienza con una vocal.
vocales = ["A", "E", "I", "O", "U"]

# Itera a través de la lista de nombres.
for nombre in lista_nombres:
    # Convierte el nombre a mayúsculas para hacer la comparación más sencilla.
    nombre = nombre.upper()
    # Verifica si el nombre comienza con una vocal.
    if nombre[0] in vocales:
        # Agrega las primeras tres letras del nombre a la lista nombres_vocales.
        nombres_vocales.append(nombre[:3])

# Imprime la lista resultante.
print(nombres_vocales)
