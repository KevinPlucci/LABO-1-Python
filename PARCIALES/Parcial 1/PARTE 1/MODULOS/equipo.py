# equipo.py
import json
import re
import csv
from estadisticas import Estadisticas
from jugador import Jugador


class Equipo:
    def __init__(self, json_file):
        self._jugadores = []
        try:
            self.cargar_jugadores_desde_json(json_file)
        except Exception as e:
            print(f"Error al cargar jugadores desde JSON: {str(e)}")

    # Resto de métodos...

    # Getter para obtener la lista de jugadores
    @property
    def jugadores(self):
        return self._jugadores

    # Setter para modificar la lista de jugadores
    @jugadores.setter
    def jugadores(self, value):
        self._jugadores = value

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
            print(
                "Jugadores cargados correctamente."
            )  # Agregar esta línea para depuración
        except FileNotFoundError:
            print(f"Error: El archivo JSON '{json_file}' no se encuentra.")
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON: {str(e)}")

    def mostrar_jugadores(self):
        for jugador in self.jugadores:
            print(f"{jugador.nombre}-{jugador.posicion}")

    def mostrar_estadisticas_jugador(self, index):
        jugador = self.jugadores[index]
        estadisticas = jugador.estadisticas
        print(f"Estadísticas de {jugador.nombre}:")
        print(f"Temporadas jugadas: {estadisticas.temporadas}")
        print(f"Puntos totales: {estadisticas.puntos_totales}")
        print(
            f"Promedio de puntos por partido: {estadisticas.promedio_puntos_por_partido}"
        )
        print(f"Rebotes totales: {estadisticas.rebotes_totales}")
        print(
            f"Promedio de asistencias por partido: {estadisticas.promedio_asistencias_por_partido}"
        )
        print(f"Robos totales: {estadisticas.robos_totales}")
        print(f"Bloqueos totales: {estadisticas.bloqueos_totales}")
        print(f"Porcentaje de tiros de campo: {estadisticas.porcentaje_tiros_de_campo}")
        print(f"Porcentaje de tiros libres: {estadisticas.porcentaje_tiros_libres}")
        print(f"Porcentaje de tiros triples: {estadisticas.porcentaje_tiros_triples}")

    def guardar_estadisticas_csv(self, index, filename):
        try:
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
        except (FileNotFoundError, IndexError):
            print("Error: Archivo o índice inválido.")
        except Exception as e:
            print(f"Error al guardar estadísticas en CSV: {str(e)}")

    def buscar_jugador_por_nombre(self, nombre):
        jugador_encontrado = False
        for jugador in self.jugadores:
            if re.search(nombre, jugador.nombre, re.IGNORECASE):
                print(f"Logros de {jugador.nombre}:")
                for logro in jugador.logros:
                    print(logro)
                jugador_encontrado = True
        if not jugador_encontrado:
            print(f"No se encontró ningún jugador con el nombre '{nombre}'.")

    def calcular_promedio_puntos_por_equipo_ordenado(equipo):
        # Calcular el promedio de puntos por partido para cada jugador y almacenarlos en una lista
        promedios = []
        for jugador in equipo.jugadores:
            estadisticas = jugador.estadisticas
            if estadisticas.temporadas > 0:
                promedio = estadisticas.puntos_totales / estadisticas.temporadas
                promedios.append((jugador.nombre, promedio))

        # Ordenar el equipo por nombre en orden ascendente
        equipo_ordenado = sorted(promedios, key=lambda x: x[0])

        return equipo_ordenado

    def imprimir_promedio_puntos_equipo(self):
        equipo_ordenado = self.calcular_promedio_puntos_por_equipo_ordenado()
        if equipo_ordenado:
            print(
                "Promedio de puntos por partido del equipo, ordenado por nombre de manera ascendente:"
            )
            for nombre, promedio in equipo_ordenado:
                print(f"{nombre}: {promedio:.2f}")

            # Calcular el promedio del equipo
            promedio_equipo = sum(promedio for _, promedio in equipo_ordenado) / len(
                equipo_ordenado
            )
            promedio_redondeado = round(promedio_equipo, 2)
            print(
                f"El promedio de puntos por partido del equipo es: {promedio_redondeado:.2f}"
            )
        else:
            print("No hay datos disponibles para calcular el promedio del equipo.")

    def es_miembro_hall_of_fame(self, nombre):
        for jugador in self.jugadores:
            if jugador.nombre.lower() == nombre.lower():
                for logro in jugador.logros:
                    if (
                        "Miembro del Salon de la Fama del Baloncesto" in logro
                        and "Universitario" not in logro
                    ):
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
