# Crea un diccionario que contenga el nombre y el sueldo de varios empleados.
# Luego, permite al usuario aumentar el sueldo de un empleado y actualizar el valor correspondiente en el diccionario.

# Crear un diccionario con nombres de empleados y sus sueldos
empleados = {"Juan": 50000, "María": 55000, "Pedro": 48000, "Ana": 52000}

# Mostrar la lista de empleados y sus sueldos
print("Lista de empleados y sus sueldos:")
for nombre, sueldo in empleados.items():
    print("{}: ${}".format(nombre, sueldo))

# Pedir al usuario el nombre del empleado y el aumento de sueldo
nombre_empleado = input(
    "Ingrese el nombre del empleado al que desea aumentar el sueldo: "
)
aumento_sueldo = float(input("Ingrese la cantidad del aumento de sueldo: "))

# Verificar si el empleado existe en el diccionario
if nombre_empleado in empleados:
    # Aumentar el sueldo del empleado
    empleados[nombre_empleado] += aumento_sueldo
    print(
        "El sueldo de {} ha sido aumentado a ${}".format(
            nombre_empleado, empleados[nombre_empleado]
        )
    )
else:
    print("El empleado '{}' no existe en la lista.".format(nombre_empleado))

# Mostrar la lista actualizada de empleados y sus sueldos
print("\nLista de empleados actualizada:")
for nombre, sueldo in empleados.items():
    print("{}: ${}".format(nombre, sueldo))
