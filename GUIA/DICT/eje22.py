# Crea un diccionario que represente los gastos de una persona en diferentes categorías, donde las claves son los nombres de las categorías y los valores son los gastos correspondientes.
# Calcula el total de gastos de la persona en el mes.

# Crear un diccionario con gastos en diferentes categorías
gastos_persona = {
    "Comida": 200,
    "Transporte": 100,
    "Entretenimiento": 50,
    "Compras": 300,
    "Facturas": 150,
}

# Calcular el total de gastos de la persona en el mes
total_gastos = sum(gastos_persona.values())

# Mostrar la lista de gastos en cada categoría
print("Lista de gastos en cada categoría:")
for categoria, gasto in gastos_persona.items():
    print("{}: ${}".format(categoria, gasto))

# Mostrar el total de gastos en el mes
print("\nTotal de gastos de la persona en el mes: ${}".format(total_gastos))
