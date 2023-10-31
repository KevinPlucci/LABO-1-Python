# main.py
import re  # Importar el módulo 're' para expresiones regulares
from equipo import Equipo  # Importar la clase 'Equipo' desde el módulo 'equipo'

if __name__ == "__main__":
    # Crear una instancia de la clase 'Equipo' al cargar un archivo JSON con los datos del equipo
    equipo = Equipo("dream_team.json")

    while True:
        print("\nMenú de opciones:")
        print("1. Mostrar la lista de todos los jugadores del Dream Team")
        print("2. Mostrar estadísticas de un jugador por índice")
        print("3. Guardar estadísticas de un jugador en CSV")
        print("4. Buscar jugador por nombre")
        print("5. Calcular promedio de puntos por partido del equipo")
        print("6. Verificar si un jugador es miembro del Salón de la Fama")
        print("7. Encontrar el jugador con más rebotes totales")
        print("8. Salir")

        opcion = input("Selecciona una opción (1-8): ")

        if opcion == "1":
            print("Mostrando la lista de todos los jugadores del Dream Team:")
            equipo.mostrar_jugadores()
            print("Lista de jugadores mostrada correctamente.")
            continue  # Salta a la siguiente iteración del bucle

        if opcion == "2":
            index = input("Ingresa el índice del jugador: ")

            # Validación usando una expresión regular para asegurarse de que el índice sea un número válido
            if re.match(r"^\d+$", index):
                index = int(index)
                if 0 <= index < len(equipo.jugadores):
                    equipo.mostrar_estadisticas_jugador(index)
                    continue  # Salta a la siguiente iteración del bucle
                else:
                    print("Índice fuera de rango.")
            else:
                print("Índice inválido. Debe ser un número entero positivo.")

        if opcion == "3":
            index = input("Ingresa el índice del jugador a guardar en CSV: ")

            try:
                index = int(index)
                if 0 <= index < len(equipo.jugadores):
                    filename = input("Ingresa el nombre del archivo CSV: ")
                    equipo.guardar_estadisticas_csv(index, filename)
                    # Salir del bucle interno después de guardar el CSV
                    continue  # Salta a la siguiente iteración del bucle
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Índice inválido.")

        if opcion == "4":
            nombre = input("Ingresa el nombre completo del jugador a buscar: ")

            # Validación usando una expresión regular
            # Permite letras mayúsculas y minúsculas, espacios, guiones y apóstrofes, y requiere al menos un espacio
            if re.match(r"^[a-zA-Z\s\'-]+ [a-zA-Z\s\'-]+$", nombre):
                equipo.buscar_jugador_por_nombre(nombre)
                continue
            else:
                print(
                    "Nombre inválido. Debe contener al menos un espacio y solo letras, espacios, guiones y apóstrofes."
                )

        if opcion == "5":
            equipo.imprimir_promedio_puntos_equipo()

        elif opcion == "6":
            nombre = input(
                "Ingresa el nombre del jugador a verificar en el Salón de la Fama: "
            )

            # Validación usando una expresión regular
            # Permite letras mayúsculas y minúsculas, espacios, guiones y apóstrofes
            expresion_regular = r"^[a-zA-Z\s'-]+$"

            if re.match(expresion_regular, nombre):
                if equipo.es_miembro_hall_of_fame(nombre):
                    print(f"{nombre} es miembro del Salón de la Fama.")
                else:
                    print(f"{nombre} no es miembro del Salón de la Fama.")
            else:
                print(
                    "Nombre inválido. Debe contener solo letras, espacios, guiones y apóstrofes."
                )

        elif opcion == "7":
            equipo.jugador_con_mas_rebotes()

        elif opcion == "8":
            break

        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
