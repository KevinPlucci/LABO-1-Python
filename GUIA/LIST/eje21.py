# Crear un programa que solicite al usuario ingresar precio unitario y cantidad de 5 productos. Almacenar cada valor en dos listas distintas. Luego imprimir el precio total de cada artículo.

# Crear dos listas vacías para almacenar los precios unitarios y las cantidades
precios_unitarios = []
cantidades = []

# Solicitar al usuario ingresar el precio unitario y la cantidad de 5 productos
for i in range(5):
    precio = float(input(f"Ingrese el precio unitario del producto {i+1}: "))
    cantidad = int(input(f"Ingrese la cantidad del producto {i+1}: "))

    precios_unitarios.append(precio)
    cantidades.append(cantidad)

# Calcular e imprimir el precio total de cada artículo
print("\nPrecio total de cada artículo:")
for i in range(5):
    precio_total = precios_unitarios[i] * cantidades[i]
    print(f"Producto {i+1}: ${precio_total:.2f}")
