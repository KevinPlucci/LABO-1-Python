from data_stark import lista_personajes


# Función para imprimir la lista de superhéroes de un género dado
def listar_superheroes_genero(genero):
    for personaje in lista_personajes:
        if personaje["genero"] == genero:
            print(personaje["nombre"])


# Función para encontrar el superhéroe más alto de un género dado
def encontrar_superheroe_mas_alto(genero):
    altura_max = 0
    nombre_superheroe = ""
    for personaje in lista_personajes:
        if personaje["genero"] == genero:
            altura = float(personaje["altura"])
            if altura > altura_max:
                altura_max = altura
                nombre_superheroe = personaje["nombre"]
    return nombre_superheroe


# Función para encontrar el superhéroe más bajo de un género dado
def encontrar_superheroe_mas_bajo(genero):
    altura_min = float("inf")
    nombre_superheroe = ""
    for personaje in lista_personajes:
        if personaje["genero"] == genero:
            altura = float(personaje["altura"])
            if altura < altura_min:
                altura_min = altura
                nombre_superheroe = personaje["nombre"]
    return nombre_superheroe


# Función para calcular la altura promedio de superhéroes de un género dado
def altura_promedio(genero):
    total_altura = 0
    total_superheroes = 0
    for personaje in lista_personajes:
        if personaje["genero"] == genero:
            total_altura += float(personaje["altura"])
            total_superheroes += 1
    if total_superheroes == 0:
        return 0
    return total_altura / total_superheroes


# Función para contar la cantidad de superhéroes por color de ojos
def contar_color_ojos():
    color_ojos_count = {}
    for personaje in lista_personajes:
        color_ojos = personaje["color_ojos"]
        if color_ojos in color_ojos_count:
            color_ojos_count[color_ojos] += 1
        else:
            color_ojos_count[color_ojos] = 1
    return color_ojos_count


# Función para contar la cantidad de superhéroes por color de pelo
def contar_color_pelo():
    color_pelo_count = {}
    for personaje in lista_personajes:
        color_pelo = personaje["color_pelo"]
        if color_pelo in color_pelo_count:
            color_pelo_count[color_pelo] += 1
        else:
            color_pelo_count[color_pelo] = 1
    return color_pelo_count


# Función para contar la cantidad de superhéroes por tipo de inteligencia
def contar_tipo_inteligencia():
    tipo_inteligencia_count = {}
    for personaje in lista_personajes:
        tipo_inteligencia = personaje["inteligencia"]
        if tipo_inteligencia == "":
            tipo_inteligencia = "No Tiene"
        if tipo_inteligencia in tipo_inteligencia_count:
            tipo_inteligencia_count[tipo_inteligencia] += 1
        else:
            tipo_inteligencia_count[tipo_inteligencia] = 1
    return tipo_inteligencia_count


# Función para listar superhéroes agrupados por cierta característica
def listar_superheroes_agrupados(caracteristica):
    agrupados = {}
    for personaje in lista_personajes:
        valor = personaje[caracteristica]
        if valor in agrupados:
            agrupados[valor].append(personaje["nombre"])
        else:
            agrupados[valor] = [personaje["nombre"]]
    return agrupados


# Menú principal
while True:
    print("\nMenú:")
    print("1. Superhéroes de género M")
    print("2. Superhéroes de género F")
    print("3. Superhéroe más alto de género M")
    print("4. Superhéroe más alto de género F")
    print("5. Superhéroe más bajo de género M")
    print("6. Superhéroe más bajo de género F")
    print("7. Altura promedio de superhéroes de género M")
    print("8. Altura promedio de superhéroes de género F")
    print("9. Cantidad de superhéroes por color de ojos")
    print("10. Cantidad de superhéroes por color de pelo")
    print("11. Cantidad de superhéroes por tipo de inteligencia")
    print("12. Listar superhéroes agrupados por color de ojos")
    print("13. Listar superhéroes agrupados por color de pelo")
    print("14. Listar superhéroes agrupados por tipo de inteligencia")
    print("0. Salir")

    opcion = input("Ingrese el número de la opción que desea ejecutar: ")

    if opcion == "1":
        print("\nSuperhéroes de género M:")
        listar_superheroes_genero("M")
    elif opcion == "2":
        print("\nSuperhéroes de género F:")
        listar_superheroes_genero("F")
    elif opcion == "3":
        print("\nSuperhéroe más alto de género M:")
        nombre_mas_alto_m = encontrar_superheroe_mas_alto("M")
        print(nombre_mas_alto_m)
    elif opcion == "4":
        print("\nSuperhéroe más alto de género F:")
        nombre_mas_alto_f = encontrar_superheroe_mas_alto("F")
        print(nombre_mas_alto_f)
    elif opcion == "5":
        print("\nSuperhéroe más bajo de género M:")
        nombre_mas_bajo_m = encontrar_superheroe_mas_bajo("M")
        print(nombre_mas_bajo_m)
    elif opcion == "6":
        print("\nSuperhéroe más bajo de género F:")
        nombre_mas_bajo_f = encontrar_superheroe_mas_bajo("F")
        print(nombre_mas_bajo_f)
    elif opcion == "7":
        print("\nAltura promedio de superhéroes de género M:")
        altura_promedio_m = altura_promedio("M")
        print(altura_promedio_m)
    elif opcion == "8":
        print("\nAltura promedio de superhéroes de género F:")
        altura_promedio_f = altura_promedio("F")
        print(altura_promedio_f)
    elif opcion == "9":
        print("\nCantidad de superhéroes por color de ojos:")
        color_ojos_count = contar_color_ojos()
        for color, count in color_ojos_count.items():
            print(f"{color}: {count}")
    elif opcion == "10":
        print("\nCantidad de superhéroes por color de pelo:")
        color_pelo_count = contar_color_pelo()
        for color, count in color_pelo_count.items():
            print(f"{color}: {count}")
    elif opcion == "11":
        print("\nCantidad de superhéroes por tipo de inteligencia:")
        tipo_inteligencia_count = contar_tipo_inteligencia()
        for tipo, count in tipo_inteligencia_count.items():
            print(f"{tipo}: {count}")
    elif opcion == "12":
        print("\nSuperhéroes agrupados por color de ojos:")
        superheroes_agrupados = listar_superheroes_agrupados("color_ojos")
        for color, heroes in superheroes_agrupados.items():
            print(f"{color}: {', '.join(heroes)}")
    elif opcion == "13":
        print("\nSuperhéroes agrupados por color de pelo:")
        superheroes_agrupados = listar_superheroes_agrupados("color_pelo")
        for color, heroes in superheroes_agrupados.items():
            print(f"{color}: {', '.join(heroes)}")
    elif opcion == "14":
        print("\nSuperhéroes agrupados por tipo de inteligencia:")
        superheroes_agrupados = listar_superheroes_agrupados("inteligencia")
        for tipo, heroes in superheroes_agrupados.items():
            print(f"{tipo}: {', '.join(heroes)}")
    elif opcion == "0":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente nuevamente.")



