"""
# Menú principal
def menu():
    archivo = "data_stark.json"
    heroes = normalizar_datos(leer_archivo(archivo))

    while True:
        print("\n--- Menú de opciones ---")
        print("1. Ordenar por altura (de menor a mayor)")
        print("2. Ordenar por peso (de mayor a menor)")
        print("3. Ordenar alfabéticamente por nombre")
        print("4. Ordenar por largo del nombre (descendente)")
        print("5. Ordenar por una clave específica")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            resultado = ordenar_por_altura(heroes)
        elif opcion == "2":
            resultado = ordenar_por_peso(heroes)
        elif opcion == "3":
            resultado = ordenar_por_nombre(heroes)
        elif opcion == "4":
            resultado = ordenar_por_largo_nombre(heroes)
        elif opcion == "5":
            clave = input("Ingrese el nombre de la clave por la que desea ordenar: ")
            ascendente = input("¿Ordenar ascendente (S/N)? ").strip().lower() == "s"
            resultado = ordenar_por_key(heroes, clave, ascendente)
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

        print("\nResultados:")
        for heroe in resultado:
            print(
                f"Nombre: {heroe['nombre']}, Altura: {heroe['altura']}, Peso: {heroe['peso']}"
            )


if __name__ == "__main__":
    menu()
"""
