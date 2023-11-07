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
        print("8. Ordenar lista de jugadores descendente y mostrar")
        print("9. Guardar lista ordenada en CSV con su apellido.csv")
        print(
            "10. Guardar lista ordenada en JSON y permitir al usuario ingresar el nombre del archivo (validar con regex)"
        )
        print("11. Ordenar los jugadores por valor sumado")
        print("12. Listar jugadores ordenados y mostrar el porcentaje de valor sumado")
        print(
            "13. Crear un filtro para mostrar jugadores por cantidad ordenados por suma de los dos campos"
        )
        print(
            "14. Mostrar las posiciones y guardarlas en SQLite(Base de datos con sus posiciones)"
        )
        print("15. Salir")

        opcion = input("Selecciona una opción (1-15): ")

        if opcion == "1":
            print("Mostrando la lista de todos los jugadores del Dream Team:")
            equipo.mostrar_jugadores()
            print("Lista de jugadores mostrada correctamente.")
            continue  # Salta a la siguiente iteración del bucle

        elif opcion == "2":
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

        elif opcion == "3":
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

        elif opcion == "4":
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

        elif opcion == "5":
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
            # A) Ordenar la lista de jugadores de manera descendente y mostrarla
            equipo.ordenar_jugadores_descendente()
            print("Lista de jugadores ordenada de manera descendente:")
            equipo.mostrar_jugadores()
            equipo.guardar_lista_jugadores_en_sqlite()
            continue

        elif opcion == "9":
            equipo.guardar_lista_jugadores_en_csv()
            continue

        elif opcion == "10":
            # C) Guardar la lista ordenada en un archivo JSON y permitir al usuario ingresar el nombre del archivo
            filename = input("Ingresa el nombre del archivo JSON (sin extensión): ")
            if re.match(r"^[a-zA-Z0-9_]+$", filename):
                equipo.guardar_lista_jugadores_en_json(f"{filename}.json")
                print(f"Lista de jugadores guardada en {filename}.json.")
            else:
                print(
                    "Nombre de archivo inválido. Debe contener solo letras, números y guiones bajos."
                )
            continue
        elif opcion == "11":
            equipo.ordenar_jugadores_por_robos_y_bloqueos()
        elif opcion == "12":
            equipo.listar_jugadores_y_mostrar_porcentaje()
        elif opcion == "13":
            cantidad = int(input("Ingresa la cantidad de jugadores a mostrar: "))
            equipo.filtrar_y_mostrar_jugadores(cantidad)
        elif opcion == "14":
            equipo.guardar_lista_posiciones_en_sqlite()
            print("Posiciones guardadas en SQLite.")
            continue
        elif opcion == "15":
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
