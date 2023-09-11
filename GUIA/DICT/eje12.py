# Crea un diccionario que represente una lista de las compras. Cada clave del diccionario debe ser el nombre de un producto y cada valor debe ser su cantidad.
# Pedir al usuario que ingrese el nombre del producto e imprimir la cantidad

# Crear un diccionario para representar la lista de compras
lista_de_compras = {}

# Pedir al usuario que ingrese elementos a la lista de compras
while True:
    producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")

    # Verificar si el usuario quiere salir del programa
    if producto.lower() == "salir":
        break

    cantidad = input("Ingrese la cantidad: ")

    # Verificar si la cantidad ingresada es un número
    if cantidad.isdigit():
        cantidad = int(cantidad)
        # Agregar el producto y la cantidad al diccionario
        lista_de_compras[producto] = cantidad
    else:
        print("La cantidad debe ser un número entero.")

# Pedir al usuario que ingrese el nombre de un producto para ver su cantidad
producto_buscar = input("Ingrese el nombre del producto que desea buscar: ")

# Buscar el producto en el diccionario y mostrar su cantidad
if producto_buscar in lista_de_compras:
    print(f"La cantidad de {producto_buscar} es: {lista_de_compras[producto_buscar]}")
else:
    print(f"{producto_buscar} no se encuentra en la lista de compras.")
