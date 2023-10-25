"""
productos_precios = {
    "Manzanas": 50.5,
    "Bananas": 30.10,
    "Naranjas": 20.0,
    "Uvas": 55.10,
    "Peras": 38.10,
    "Frutillas": 80.5,
    "Kiwi": 120.10,
    "Mangos": 50.5,
    "Sandía": 20.1,
    "Papayas": 32.5
}

# Creamos un nuevo diccionario con el descuento del 10%
productos_con_descuento = {}

for producto, precio in productos_precios.items():
    precio_con_descuento = precio * 0.9  # Aplicamos un 10% de descuento
    productos_con_descuento[producto] = precio_con_descuento

print(productos_con_descuento)

"""

productos_precios = {
    "Manzanas": 50.5,
    "Bananas": 30.10,
    "Naranjas": 20.0,
    "Uvas": 55.10,
    "Peras": 38.10,
    "Frutillas": 80.5,
    "Kiwi": 120.10,
    "Mangos": 50.5,
    "Sandía": 20.1,
    "Papayas": 32.5,
}

# Creamos un nuevo diccionario con el descuento del 10%
productos_con_descuento = {}

for producto, precio in productos_precios.items():
    precio_con_descuento = precio * 0.9  # Aplicamos un 10% de descuento
    productos_con_descuento[producto] = precio_con_descuento

print(productos_con_descuento)
