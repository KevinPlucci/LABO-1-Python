import json
import csv
import re


class Estadisticas:
    def __init__(
        self,
        puntos,
        rebotes,
        asistencias,
        robos,
        bloqueos,
        tiros_de_campo,
        tiros_libres,
        triples,
        minutos_jugados,
        partidos_jugados,
        eficiencia,
    ):
        self.puntos = puntos
        self.rebotes = rebotes
        self.asistencias = asistencias
        self.robos = robos
        self.bloqueos = bloqueos
        self.tiros_de_campo = tiros_de_campo
        self.tiros_libres = tiros_libres
        self.triples = triples
        self.minutos_jugados = minutos_jugados
        self.partidos_jugados = partidos_jugados
        self.eficiencia = eficiencia


class Jugador:
    def __init__(self, nombre, posicion, logros, estadisticas):
        self._nombre = nombre
        self._posicion = posicion
        self._logros = logros
        self._estadisticas = estadisticas


class Equipo:
    def __init__(self, json_file):
        self._jugadores = self.cargar_jugadores_desde_json(json_file)


def cargar_jugadores_json(self, json_file):
    with open(json_file, "r") as file:
        data = json.load(file)
        jugadores = []
        for jugador_data in data:
            nombre = jugador_data["nombre"]
            posicion = jugador_data["posicion"]
            logros = jugador_data["logros"]
            estadisticas_data = jugador_data["estadisticas"]
            estadisticas = Estadisticas(**estadisticas_data)
            jugador = jugador(nombre, posicion, logros, estadisticas)
            jugadores.append(jugador)
        return jugadores


def mostrar_jugadores(equipo):
    for i, jugador in enumerate(equipo.jugadores):
        print(f"{i+1}. {jugador.nombre} - {jugador.posicion}")


def mostrar_estadisticas_jugador(equipo, indice):
    jugador = equipo.jugadores[indice]
    estadisticas = jugador.estadisticas
    print(f"Estadisticas de {jugador.nombre}:")
    print(f"Temporadas jugadas {jugador.partidos_jugados}:")
    print(f"Puntos totales {jugador.puntos}:")
    # Muestra las demas estadisticas
    print(
        f"Promedio de puntos por partido:{estadisticas.puntos / estadisticas.partidos_jugados}"
    )
    print(f"Rebotes totales: {estadisticas.rebotes}")
    # Muestra el resto de las estadisticas


def guardar_estadisticas_csv(equipo, indice):
    jugador = equipo.jugadores[indice]
    estadisticas = jugador.estadisticas
    with open("jugadores_estadisticas.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "Nombre",
                "Posicion",
                "Temporada",
                "Puntos totales",
                "Promedio de puntos por partido",
                "Rebotes totales",
                "Promedio de asistencia por partidos",
                "Robos totales",
                "Bloqueos totales",
                "Porcentaje de tiros de campo",
                "Porcentaje de tiros libres",
                "Porcentaje de tiros triples",
            ]
        )


writer.writerow([jugador.nombre, jugador.posicion, estadisticas.posicion])
