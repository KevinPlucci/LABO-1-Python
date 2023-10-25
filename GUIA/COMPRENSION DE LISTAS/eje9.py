"""
Dada una lista de nombres:
lista_nombres = ["Lourdes", "Ignacio", "Adela", "Roberto", "Marina", "Ramón", "Ezequiel", "Rodrigo", "Beatriz", "Miguel"]
Crea una lista que contenga sólo los nombres que comienzan con una consonante

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

nombres_consonantes = []

consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

for nombre in lista_nombres:
    if nombre[0] in consonantes:
        nombres_consonantes.append(nombre)

print(nombres_consonantes)
