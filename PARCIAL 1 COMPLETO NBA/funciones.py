import json
import re
import csv


# Clase Estadísticas
class Estadisticas:
    def __init__(
        self,
        temporadas=0,
        puntos_totales=0,
        promedio_puntos_por_partido=0,
        rebotes_totales=0,
        promedio_rebotes_por_partido=0,
        asistencias_totales=0,
        promedio_asistencias_por_partido=0,
        robos_totales=0,
        bloqueos_totales=0,
        porcentaje_tiros_de_campo=0,
        porcentaje_tiros_libres=0,
        porcentaje_tiros_triples=0,
    ):
        self.temporadas = temporadas
        self.puntos_totales = puntos_totales
        self.promedio_puntos_por_partido = promedio_puntos_por_partido
        self.rebotes_totales = rebotes_totales
        self.promedio_rebotes_por_partido = promedio_rebotes_por_partido
        self.asistencias_totales = asistencias_totales
        self.promedio_asistencias_por_partido = promedio_asistencias_por_partido
        self.robos_totales = robos_totales
        self.bloqueos_totales = bloqueos_totales
        self.porcentaje_tiros_de_campo = porcentaje_tiros_de_campo
        self.porcentaje_tiros_libres = porcentaje_tiros_libres
        self.porcentaje_tiros_triples = porcentaje_tiros_triples

    # Define getters y setters o propiedades para cada atributo


# Clase Jugador
class Jugador:
    def __init__(self, nombre, posicion, logros, estadisticas):
        self.nombre = nombre
        self.posicion = posicion
        self.logros = logros
        self.estadisticas = estadisticas


# Clase Equipo
class Equipo:
    def __init__(self, json_file):
        self.jugadores = []
        self.cargar_jugadores_desde_json(json_file)

    def cargar_jugadores_desde_json(self, json_file):
        try:
            with open(json_file, "r") as file:
                data = json.load(file)
                for jugador_data in data["jugadores"]:
                    estadisticas_data = jugador_data["estadisticas"]
                    estadisticas = Estadisticas(**estadisticas_data)
                    jugador = Jugador(
                        jugador_data["nombre"],
                        jugador_data["posicion"],
                        jugador_data["logros"],
                        estadisticas,
                    )
                    self.jugadores.append(jugador)
        except FileNotFoundError:
            print("Error: El archivo JSON no se encuentra.")

    def mostrar_jugadores(self):
        for idx, jugador in enumerate(self.jugadores, start=1):
            print(f"{idx}. {jugador.nombre} - {jugador.posicion}")

    def mostrar_estadisticas_jugador(self, index):
        jugador = self.jugadores[index]
        estadisticas = jugador.estadisticas
        print(f"Estadísticas de {jugador.nombre}:")
        print(f"Temporadas jugadas: {estadisticas.temporadas}")
        print(f"Puntos totales: {estadisticas.puntos_totales}")
        print(
            f"Promedio de puntos por partido: {estadisticas.promedio_puntos_por_partido}"
        )

    def guardar_estadisticas_csv(self, index, filename):
        jugador = self.jugadores[index]
        estadisticas = jugador.estadisticas

        with open(f"{filename}.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "nombre",
                    "posicion",
                    "temporadas",
                    "puntos_totales",
                    "promedio_puntos_por_partido",
                    "rebotes_totales",
                    "promedio_rebotes_por_partido",
                    "asistencias_totales",
                    "promedio_asistencias_por_partido",
                    "robos_totales",
                    "bloqueos_totales",
                    "porcentaje_tiros_de_campo",
                    "porcentaje_tiros_libres",
                    "porcentaje_tiros_triples",
                ]
            )
            writer.writerow(
                [
                    jugador.nombre,
                    jugador.posicion,
                    estadisticas.temporadas,
                    estadisticas.puntos_totales,
                    estadisticas.promedio_puntos_por_partido,
                    estadisticas.rebotes_totales,
                    estadisticas.promedio_rebotes_por_partido,
                    estadisticas.asistencias_totales,
                    estadisticas.promedio_asistencias_por_partido,
                    estadisticas.robos_totales,
                    estadisticas.bloqueos_totales,
                    estadisticas.porcentaje_tiros_de_campo,
                    estadisticas.porcentaje_tiros_libres,
                    estadisticas.porcentaje_tiros_triples,
                ]
            )

        print(f"Estadísticas de {jugador.nombre} guardadas en {filename}.csv")

    def buscar_jugador_por_nombre(self, nombre):
        for jugador in self.jugadores:
            if re.search(nombre, jugador.nombre, re.IGNORECASE):
                print(f"Logros de {jugador.nombre}:")
                for logro in jugador.logros:
                    print(logro)

    def promedio_puntos_por_equipo(self):
        total_puntos = sum(
            jugador.estadisticas.puntos_totales for jugador in self.jugadores
        )
        total_temporadas = sum(
            jugador.estadisticas.temporadas for jugador in self.jugadores
        )
        promedio_equipo = total_puntos / total_temporadas
        return promedio_equipo

    def es_miembro_hall_of_fame(self, nombre):
        for jugador in self.jugadores:
            if jugador.nombre.lower() == nombre.lower():
                for logro in jugador.logros:
                    if "Miembro del Salon de la Fama del Baloncesto" in logro:
                        return True
        return False

    def jugador_con_mas_rebotes(self):
        max_rebotes = 0
        max_rebotes_jugador = None
        for jugador in self.jugadores:
            if jugador.estadisticas.rebotes_totales > max_rebotes:
                max_rebotes = jugador.estadisticas.rebotes_totales
                max_rebotes_jugador = jugador
        if max_rebotes_jugador:
            print(
                f"{max_rebotes_jugador.nombre} tiene la mayor cantidad de rebotes totales ({max_rebotes})."
            )


if __name__ == "__main__":
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
            equipo.mostrar_jugadores()
        elif opcion == "2":
            index = input("Ingresa el índice del jugador: ")
            try:
                index = int(index)
                if 0 <= index < len(equipo.jugadores):
                    equipo.mostrar_estadisticas_jugador(index)
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Índice inválido.")
        elif opcion == "3":
            index = input("Ingresa el índice del jugador a guardar en CSV: ")
            try:
                index = int(index)
                if 0 <= index < len(equipo.jugadores):
                    filename = input("Ingresa el nombre del archivo CSV: ")
                    equipo.guardar_estadisticas_csv(index, filename)
                    print(
                        f"Estadísticas de {equipo.jugadores[index].nombre} guardadas en {filename}."
                    )
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Índice inválido.")
        elif opcion == "4":
            nombre = input("Ingresa el nombre del jugador a buscar: ")
            equipo.buscar_jugador_por_nombre(nombre)
        elif opcion == "5":
            promedio_equipo = equipo.promedio_puntos_por_equipo()
            promedio_redondeado = round(promedio_equipo, 2)  # Redondea a dos decimales
            print(
                f"El promedio de puntos por partido del equipo es: {promedio_redondeado}"
            )
        elif opcion == "6":
            nombre = input(
                "Ingresa el nombre del jugador a verificar en el Salón de la Fama: "
            )
            if equipo.es_miembro_hall_of_fame(nombre):
                print(f"{nombre} es miembro del Salón de la Fama.")
            else:
                print(f"{nombre} no es miembro del Salón de la Fama.")
        elif opcion == "7":
            equipo.jugador_con_mas_rebotes()
        elif opcion == "8":
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
