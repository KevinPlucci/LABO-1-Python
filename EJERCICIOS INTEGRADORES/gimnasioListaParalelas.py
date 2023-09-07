# Listas para almacenar la información de los miembros
numeros_identificacion = []
nombres = []
edades = []
tipos_membresia = []

while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Agregar un nuevo miembro")
    print("2. Mostrar la información de todos los miembros")
    print("3. Actualizar el tipo de membresía de un miembro")
    print("4. Buscar información de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar el miembro más joven y el más viejo")
    print("0. Salir del programa")

    opcion = input("\nIngrese la opción deseada: ")

    # Opción 1: Agregar un nuevo miembro
    if opcion == "1":
        id_nuevo = input("Ingrese el número de identificación del nuevo miembro: ")
        nombre_nuevo = input("Ingrese el nombre del nuevo miembro: ")
        edad_nueva = int(input("Ingrese la edad del nuevo miembro: "))
        membresia_nueva = input("Ingrese el tipo de membresía del nuevo miembro: ")

        # Agregar información a las listas
        numeros_identificacion.append(id_nuevo)
        nombres.append(nombre_nuevo)
        edades.append(edad_nueva)
        tipos_membresia.append(membresia_nueva)
        print("Nuevo miembro agregado con éxito.")

    # Opción 2: Mostrar la información de todos los miembros
    elif opcion == "2":
        print("Nro ID.\tNombre\tEdad\tTipo membresía")
        for i in range(len(numeros_identificacion)):
            print(
                f"{numeros_identificacion[i]}\t{nombres[i]}\t{edades[i]}\t{tipos_membresia[i]}"
            )

    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        id_actualizar = input(
            "Ingrese el número de identificación del miembro a actualizar: "
        )
        if id_actualizar in numeros_identificacion:
            indice = numeros_identificacion.index(id_actualizar)
            nuevo_tipo_membresia = input("Ingrese el nuevo tipo de membresía: ")
            tipos_membresia[indice] = nuevo_tipo_membresia
            print("Tipo de membresía actualizado con éxito.")
        else:
            print("El miembro no se encontró.")

    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        id_buscar = input("Ingrese el número de identificación del miembro a buscar: ")
        if id_buscar in numeros_identificacion:
            indice = numeros_identificacion.index(id_buscar)
            print("Información del miembro:")
            print(f"Nro ID: {numeros_identificacion[indice]}")
            print(f"Nombre: {nombres[indice]}")
            print(f"Edad: {edades[indice]}")
            print(f"Tipo membresía: {tipos_membresia[indice]}")
        else:
            print("El miembro no se encontró.")

    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        if len(edades) > 0:
            promedio = sum(edades) / len(edades)
            print(f"El promedio de edad de los miembros es: {promedio}")
        else:
            print("No hay miembros registrados.")

    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        if len(edades) > 0:
            indice_mas_joven = edades.index(min(edades))
            indice_mas_viejo = edades.index(max(edades))
            print("Miembro más joven:")
            print(f"Nro ID: {numeros_identificacion[indice_mas_joven]}")
            print(f"Nombre: {nombres[indice_mas_joven]}")
            print(f"Edad: {edades[indice_mas_joven]}")
            print(f"Tipo membresía: {tipos_membresia[indice_mas_joven]}")
            print("Miembro más viejo:")
            print(f"Nro ID: {numeros_identificacion[indice_mas_viejo]}")
            print(f"Nombre: {nombres[indice_mas_viejo]}")
            print(f"Edad: {edades[indice_mas_viejo]}")
            print(f"Tipo membresía: {tipos_membresia[indice_mas_viejo]}")
        else:
            print("No hay miembros registrados.")

    # Opción 0: Salir
    elif opcion == "0":
        break

    else:
        print("Opción inválida. Intente de nuevo.")
