"""Ejercicio Integrador 01

La división de higiene está trabajando en un control de stock para productos sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
El tipo (validar "barbijo", "jabón" o "alcohol")
El precio: (validar entre 100 y 300)
La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
La marca y el Fabricante.
Se debe informar lo siguiente:
Del más caro de los barbijos, la cantidad de unidades y el fabricante.
Del ítem con más unidades, el fabricante.
Cuántas unidades de jabones hay en total.
"""
# Inicializamos variables para almacenar la información deseada
max_precio_barbijo = 0
cantidad_max_precio_barbijo = 0
fabricante_max_precio_barbijo = ""
max_unidades = 0
fabricante_max_unidades = ""
total_jabones = 0

# Realizamos la carga de datos para 5 productos
for i in range(5):
    print(f"Ingrese los datos del producto {i + 1}:")

    # Validación del tipo de producto
    while True:
        tipo = input("Tipo de producto (barbijo, jabón o alcohol): ")
        if tipo.lower() in ["barbijo", "jabón", "alcohol"]:
            break
        else:
            print("Tipo de producto no válido. Intente nuevamente.")

    # Validación del precio
    while True:
        precio = float(input("Precio (entre 100 y 300): "))
        if 100 <= precio <= 300:
            break
        else:
            print("Precio fuera del rango válido. Intente nuevamente.")

    # Validación de la cantidad de unidades
    while True:
        cantidad = int(input("Cantidad de unidades (entre 1 y 1000): "))
        if 1 <= cantidad <= 1000:
            break
        else:
            print("Cantidad de unidades fuera del rango válido. Intente nuevamente.")

    marca = input("Marca: ")
    fabricante = input("Fabricante: ")

    # Actualizamos la información solicitada
    if tipo.lower() == "barbijo" and precio > max_precio_barbijo:
        max_precio_barbijo = precio
        cantidad_max_precio_barbijo = cantidad
        fabricante_max_precio_barbijo = fabricante

    if cantidad > max_unidades:
        max_unidades = cantidad
        fabricante_max_unidades = fabricante

    if tipo.lower() == "jabón":
        total_jabones += cantidad

# Mostramos la información solicitada
print(
    f"Del barbijo más caro, la cantidad de unidades es {cantidad_max_precio_barbijo} y el fabricante es {fabricante_max_precio_barbijo}."
)
print(f"Del ítem con más unidades, el fabricante es {fabricante_max_unidades}.")
print(f"Total de unidades de jabones: {total_jabones}")
