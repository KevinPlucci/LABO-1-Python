# Crea un diccionario que represente los contactos de un teléfono, donde las claves son los nombres de las personas y los valores son los números de teléfono correspondientes.
# Solicitar al usuario el nombre de un contacto: agregarlo al diccionario en caso de que no exista. En caso de que exista modificar el número de teléfono del contacto.

# Crear un diccionario con contactos de teléfono
contactos = {"Juan": "123-456-7890", "María": "987-654-3210", "Pedro": "555-555-5555"}

# Mostrar la lista de contactos
print("Lista de contactos:")
for nombre, numero in contactos.items():
    print("{}: {}".format(nombre, numero))

# Solicitar al usuario el nombre de un contacto
nombre_contacto = input("Ingrese el nombre del contacto: ")
numero_telefono = input(
    "Ingrese el número de teléfono para {}: ".format(nombre_contacto)
)

# Agregar o modificar el contacto en el diccionario
contactos[nombre_contacto] = numero_telefono
print(
    "{} ha sido agregado o actualizado en la lista de contactos.".format(
        nombre_contacto
    )
)

# Mostrar la lista actualizada de contactos
print("\nLista de contactos actualizada:")
for nombre, numero in contactos.items():
    print("{}: {}".format(nombre, numero))
