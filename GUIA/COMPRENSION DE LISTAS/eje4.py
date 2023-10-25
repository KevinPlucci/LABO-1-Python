"""
Dada una lista de frutas:
lista_frutas = ["manzana", "plátano", "naranja", "uva", "sandía", "fresa", "kiwi", "pera", "mango", "papaya"]
Crea una lista que contenga sólo las palabras que tienen más de 5 letras
"""

lista_frutas = [
    "manzana",
    "plátano",
    "naranja",
    "uva",
    "sandía",
    "fresa",
    "kiwi",
    "pera",
    "mango",
    "papaya",
]

# Crear una nueva lista con frutas que tienen más de 5 letras
frutas_mas_de_5_letras = [fruta for fruta in lista_frutas if len(fruta) > 5]

print(frutas_mas_de_5_letras)
