# DICT
dict_alumno = {"edad": 22, "legajo": 205664, "nombre": "Juan", "apellido": "Perez"}
print(
    "El legajo es {0}, el nombre es {1} y el apellido es {2}".format(
        dict_alumno["legajo"]
    ),
    dict_alumno["nombre"],
    dict_alumno["apellido"],
)

dict_alumno["cuit"] = "22-123334444-9"

print(
    "El legajo es {1}, el nombre es {2} y el apellido es {3} y el cuit es {0}".format(
        dict_alumno["legajo"],
        dict_alumno["cuit"],
        dict_alumno["legajo"],
        dict_alumno["nombre"],
        dict_alumno["apellido"],
    )
)

claves = dict_alumno.keys()
print(claves)
for clave in dict_alumno.keys():
    print(dict_alumno[clave])

for clave, valor in dict_alumno.items():
    print("La clave: {0} tiene el valor: {1}".format(clave, valor))
