# Crea un diccionario que contenga la información de una dirección: nombre de la calle, altura, localidad, código postal, partido y provincia. Luego, imprime el nombre de la calle, seguido de su altura.

# Crear el diccionario de información de la dirección
direccion = {
    "nombre_calle": "Calle Ejemplo",
    "altura": 123,
    "localidad": "Ciudad Ejemplo",
    "codigo_postal": "12345",
    "partido": "Partido Ejemplo",
    "provincia": "Provincia Ejemplo",
}

# Imprimir el nombre de la calle seguido de su altura
print(f"Dirección: {direccion['nombre_calle']} {direccion['altura']}")
