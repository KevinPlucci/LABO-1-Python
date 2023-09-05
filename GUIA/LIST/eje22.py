"""
    Crear un programa que solicite al usuario ingresar: nombre del producto, cantidad y precio unitario. Guardar los datos en 3 listas distintas.
    Solicitar productos hasta que el nombre del producto sea ‘xxx’. Luego imprimir la lista de artículos con el siguiente formato:
nombre_articulo	cantidad	$ precio_unitario 	$ total
	Ejemplo:
	alfajor capitan del espacio		6	$ 150		$ 900
    …
"""

# Crear listas para almacenar los datos de los productos
nombres_productos = []
cantidades = []
precios_unitarios = []

# Solicitar al usuario ingresar productos hasta que se ingrese 'xxx'
while True:
    nombre = input("Ingrese el nombre del producto ('xxx' para finalizar): ")
    if nombre == "xxx":
        break

    cantidad = int(input(f"Ingrese la cantidad de '{nombre}': "))
    precio = float(input(f"Ingrese el precio unitario de '{nombre}': $"))

    # Almacenar los datos en las listas
    nombres_productos.append(nombre)
    cantidades.append(cantidad)
    precios_unitarios.append(precio)

# Imprimir la lista de artículos en el formato especificado
print("\nLista de artículos:")
print(
    "{:<30} {:<10} {:<15} {:<10}".format(
        "Nombre Artículo", "Cantidad", "$ Precio Unitario", "$ Total"
    )
)
for i in range(len(nombres_productos)):
    nombre = nombres_productos[i]
    cantidad = cantidades[i]
    precio_unitario = precios_unitarios[i]
    total = cantidad * precio_unitario
    print(
        "{:<30} {:<10} {:<15.2f} {:<10.2f}".format(
            nombre, cantidad, precio_unitario, total
        )
    )
