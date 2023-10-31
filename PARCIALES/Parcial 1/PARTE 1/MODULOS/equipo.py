# equipo.py
import json
import re
import csv
from estadisticas import Estadisticas
from jugador import Jugador


class Equipo:
    def __init__(self, json_file):
        """
        Inicializa una instancia de la clase Equipo y carga los datos de los jugadores desde un archivo JSON.

        :param json_file: Ruta al archivo JSON que contiene los datos de los jugadores.
        """
        self._jugadores = []
        try:
            self.cargar_jugadores_desde_json(json_file)
        except Exception as e:
            print(f"Error al cargar jugadores desde JSON: {str(e)}")

    @property
    def jugadores(self):
        """
        Getter para obtener la lista de jugadores del equipo.

        :return: La lista de jugadores del equipo.
        """
        return self._jugadores

    @jugadores.setter
    def jugadores(self, value):
        """
        Setter para modificar la lista de jugadores del equipo.

        :param value: La nueva lista de jugadores que reemplazará a la lista existente.
        """
        self._jugadores = value

    def cargar_jugadores_desde_json(self, json_file):
        """
        Carga los datos de los jugadores desde un archivo JSON y crea instancias de la clase Jugador para cada jugador.

        :param json_file: Ruta al archivo JSON que contiene los datos de los jugadores.
        """
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
            print("Jugadores cargados correctamente.")
        except FileNotFoundError:
            print(f"Error: El archivo JSON '{json_file}' no se encuentra.")
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON: {str(e)}")

    def mostrar_jugadores(self):
        """
        Muestra en la consola los nombres y posiciones de todos los jugadores del equipo.
        """
        for jugador in self.jugadores:
            print(f"{jugador.nombre}-{jugador.posicion}")

    def mostrar_estadisticas_jugador(self, index):
        """
        Muestra en la consola las estadísticas de un jugador específico del equipo.

        :param index: El índice del jugador en la lista de jugadores.
        """
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
        """
        Guarda las estadísticas de un jugador específico en un archivo CSV.

        :param index: El índice del jugador en la lista de jugadores.
        :param filename: El nombre del archivo CSV donde se guardarán las estadísticas.
        """
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
        """
        Busca un jugador por nombre y muestra en la consola los logros del jugador si se encuentra.

        :param nombre: El nombre del jugador que se está buscando.
        """
        jugador_encontrado = False
        for jugador in self.jugadores:
            if re.search(nombre, jugador.nombre, re.IGNORECASE):
                print(f"Logros de {jugador.nombre}:")
                for logro in jugador.logros:
                    print(logro)
                jugador_encontrado = True
        if not jugador_encontrado:
            print(f"No se encontró ningún jugador con el nombre '{nombre}'.")

    # En tu archivo JSON, asegúrate de que tengas una clave "promedio_puntos_por_partido" para cada jugador, por ejemplo:
    # "promedio_puntos_por_partido": 20.5

    @staticmethod
    def calcular_promedio_puntos_por_equipo_ordenado(jugadores):
        """
        Obtiene el promedio de puntos por partido para cada jugador del equipo y devuelve una lista ordenada por nombre de jugador.

        :param jugadores: La lista de jugadores del equipo.
        :return: Una lista ordenada con los promedios de puntos por partido de cada jugador.
        """
        promedios = []
        for jugador in jugadores:
            promedio = jugador.estadisticas.promedio_puntos_por_partido
            promedios.append((jugador.nombre, promedio))

        equipo_ordenado = sorted(promedios, key=lambda x: x[0])
        return equipo_ordenado

    def imprimir_promedio_puntos_equipo(self):
        """
        Muestra en la consola el promedio de puntos por partido del equipo, ordenado alfabéticamente por nombre.
        """
        equipo_ordenado = Equipo.calcular_promedio_puntos_por_equipo_ordenado(
            self.jugadores
        )
        if equipo_ordenado:
            print(
                "Promedio de puntos por partido del equipo, ordenado por nombre de manera ascendente:"
            )
            for nombre, promedio in equipo_ordenado:
                print(f"{nombre}: {promedio:.2f}")

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
        """
        Comprueba si un jugador es miembro del Salón de la Fama del Baloncesto.

        :param nombre: El nombre del jugador que se está comprobando.
        :return: True si el jugador es miembro, False en caso contrario.
        """
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
        """
        Encuentra al jugador con la mayor cantidad de rebotes totales en el equipo y muestra su nombre y la cantidad de rebotes en la consola.
        """
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
