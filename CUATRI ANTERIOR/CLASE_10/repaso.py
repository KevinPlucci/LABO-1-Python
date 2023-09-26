lista = [
    {"title": "QUEVEDO || BZRP Music Sessions #52", "views": 505192970, "length": 204},
    {
        "title": "VILLANO ANTILLANO || BZRP Music Sessions #51",
        "views": 201947399,
        "length": 188,
    },
]

with open("prueba.csv", "w") as file:
    for elemento in lista:
        file.write(
            "{0},{1},{2}\n".format(
                elemento["title"], elemento["views"], elemento["length"]
            )
        )


lista_palabras = ["hola", "perro", "gato", "carolina"]
print(",".join(lista_palabras))

with open("prueba.csv", "w") as file:
    if len(lista_palabras) > 0:
        file.write("{0}".format(lista_palabras[0]))
        for elemento in lista_palabras[1:]:
            file.write(",{0}".format(elemento))


with open("prueba.csv", "w") as file:
    if len(lista_palabras) > 0:
        file.write(",".join(lista_palabras))


lista = [
    {"title": "QUEVEDO || BZRP Music Sessions #52", "views": 505192970, "length": 204},
    {
        "title": "VILLANO ANTILLANO || BZRP Music Sessions #51",
        "views": 201947399,
        "length": 188,
    },
    {"title": "DUKI || BZRP Music Sessions #50", "views": 81192970, "length": 232},
]

lista_aux = []
for elemento in lista:
    lista_aux.append(elemento["length"])

print(lista_aux)


lista_temas = [
    {"title": "QUEVEDO || BZRP Music Sessions #52", "views": 100, "length": 20},
    {
        "title": "VILLANO ANTILLANO || BZRP Music Sessions #51",
        "views": 200,
        "length": 10,
    },
    {
        "title": "DUKI || BZRP Music Sessions #50",
        "views": 100,
        "length": 15,
        "nolike": 15,
    },
]


def calcula_promedio(lista: list, key: str) -> float:
    acumulador = 0
    contador = 0
    resultado = 0
    if len(lista) == 0:
        return 0
    for elemento in lista:
        if key in elemento:
            if type(elemento[key]) == type(int()) or type(elemento[key]) == type(
                float()
            ):
                acumulador += elemento[key]
                contador += 1
    if contador > 0:
        resultado = acumulador / contador

    return resultado


print("El promedio de longitud es {0}".format(calcula_promedio(lista_temas, "length")))
print("El promedio de views es {0}".format(calcula_promedio(lista_temas, "views")))
print("El promedio de No LIKE es {0}".format(calcula_promedio(lista_temas, "nolike")))
print(
    "El promedio que no existe es {0}".format(calcula_promedio(lista_temas, "sarasa"))
)

print("SUPERAN EL PROMEDIO")
promedio_views = calcula_promedio(lista_temas, "views")
for elemento in lista_temas:
    if elemento["views"] > promedio_views:
        print(
            "{0},{1},{2}\n".format(
                elemento["title"], elemento["views"], elemento["length"]
            )
        )
