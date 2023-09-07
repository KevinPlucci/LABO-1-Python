# Importa la lista de superhéroes desde data_stark.py
from data_stark import lista_personajes


# Función para imprimir el nombre de cada superhéroe
def imprimir_nombres():
    for heroe in lista_personajes:
        print(heroe["nombre"])


# Función para imprimir el nombre y la altura de cada superhéroe
def imprimir_nombre_altura():
    for heroe in lista_personajes:
        print(f"{heroe['nombre']} - Altura: {heroe['altura']} cm")


# Función para encontrar el superhéroe más alto
def encontrar_maxima_altura():
    max_altura = 0
    heroe_max = None
    for heroe in lista_personajes:
        altura = float(heroe["altura"])
        if altura > max_altura:
            max_altura = altura
            heroe_max = heroe
    return heroe_max


# Función para encontrar el superhéroe más bajo
def encontrar_minima_altura():
    min_altura = float("inf")
    heroe_min = None
    for heroe in lista_personajes:
        altura = float(heroe["altura"])
        if altura < min_altura:
            min_altura = altura
            heroe_min = heroe
    return heroe_min


# Función para calcular la altura promedio de los superhéroes
def calcular_altura_promedio():
    total_altura = 0
    for heroe in lista_personajes:
        total_altura += float(heroe["altura"])
    altura_promedio = total_altura / len(lista_personajes)
    return altura_promedio


# Función para encontrar el superhéroe más pesado
def encontrar_maximo_peso():
    max_peso = 0
    heroe_max = None
    for heroe in lista_personajes:
        peso = float(heroe["peso"])
        if peso > max_peso:
            max_peso = peso
            heroe_max = heroe
    return heroe_max


# Función para encontrar el superhéroe menos pesado
def encontrar_minimo_peso():
    min_peso = float("inf")
    heroe_min = None
    for heroe in lista_personajes:
        peso = float(heroe["peso"])
        if peso < min_peso:
            min_peso = peso
            heroe_min = heroe
    return heroe_min


# Función principal que muestra el menú y llama a las funciones correspondientes
def menu_principal():
    while True:
        print("\nMenú:")
        print("1. Imprimir nombres de superhéroes")
        print("2. Imprimir nombres y alturas de superhéroes")
        print("3. Encontrar superhéroe más alto")
        print("4. Encontrar superhéroe más bajo")
        print("5. Calcular altura promedio de superhéroes")
        print("6. Encontrar superhéroe más pesado")
        print("7. Encontrar superhéroe menos pesado")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            imprimir_nombres()
        elif opcion == "2":
            imprimir_nombre_altura()
        elif opcion == "3":
            heroe_max = encontrar_maxima_altura()
            print(
                f"Superhéroe más alto: {heroe_max['nombre']} - Altura: {heroe_max['altura']} cm"
            )
        elif opcion == "4":
            heroe_min = encontrar_minima_altura()
            print(
                f"Superhéroe más bajo: {heroe_min['nombre']} - Altura: {heroe_min['altura']} cm"
            )
        elif opcion == "5":
            altura_promedio = calcular_altura_promedio()
            print(f"Altura promedio de superhéroes: {altura_promedio} cm")
        elif opcion == "6":
            heroe_max = encontrar_maximo_peso()
            print(
                f"Superhéroe más pesado: {heroe_max['nombre']} - Peso: {heroe_max['peso']} kg"
            )
        elif opcion == "7":
            heroe_min = encontrar_minimo_peso()
            print(
                f"Superhéroe menos pesado: {heroe_min['nombre']} - Peso: {heroe_min['peso']} kg"
            )
        elif opcion == "8":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


# Ejecutar el menú principal
if __name__ == "__main__":
    menu_principal()
