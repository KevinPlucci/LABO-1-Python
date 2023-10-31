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
        self._temporadas = temporadas
        self._puntos_totales = puntos_totales
        self._promedio_puntos_por_partido = promedio_puntos_por_partido
        self._rebotes_totales = rebotes_totales
        self._promedio_rebotes_por_partido = promedio_rebotes_por_partido
        self._asistencias_totales = asistencias_totales
        self._promedio_asistencias_por_partido = promedio_asistencias_por_partido
        self._robos_totales = robos_totales
        self._bloqueos_totales = bloqueos_totales
        self._porcentaje_tiros_de_campo = porcentaje_tiros_de_campo
        self._porcentaje_tiros_libres = porcentaje_tiros_libres
        self._porcentaje_tiros_triples = porcentaje_tiros_triples

    # Getters
    @property
    def temporadas(self):
        return self._temporadas

    @property
    def puntos_totales(self):
        return self._puntos_totales

    @property
    def promedio_puntos_por_partido(self):
        return self._promedio_puntos_por_partido

    @property
    def rebotes_totales(self):
        return self._rebotes_totales

    @property
    def promedio_rebotes_por_partido(self):
        return self._promedio_rebotes_por_partido

    @property
    def asistencias_totales(self):
        return self._asistencias_totales

    @property
    def promedio_asistencias_por_partido(self):
        return self._promedio_asistencias_por_partido

    @property
    def robos_totales(self):
        return self._robos_totales

    @property
    def bloqueos_totales(self):
        return self._bloqueos_totales

    @property
    def porcentaje_tiros_de_campo(self):
        return self._porcentaje_tiros_de_campo

    @property
    def porcentaje_tiros_libres(self):
        return self._porcentaje_tiros_libres

    @property
    def porcentaje_tiros_triples(self):
        return self._porcentaje_tiros_triples

    # Setters
    @temporadas.setter
    def temporadas(self, value):
        self._temporadas = value

    @puntos_totales.setter
    def puntos_totales(self, value):
        self._puntos_totales = value

    @promedio_puntos_por_partido.setter
    def promedio_puntos_por_partido(self, value):
        self._promedio_puntos_por_partido = value

    @rebotes_totales.setter
    def rebotes_totales(self, value):
        self._rebotes_totales = value

    @promedio_rebotes_por_partido.setter
    def promedio_rebotes_por_partido(self, value):
        self._promedio_rebotes_por_partido = value

    @asistencias_totales.setter
    def asistencias_totales(self, value):
        self._asistencias_totales = value

    @promedio_asistencias_por_partido.setter
    def promedio_asistencias_por_partido(self, value):
        self._promedio_asistencias_por_partido = value

    @robos_totales.setter
    def robos_totales(self, value):
        self._robos_totales = value

    @bloqueos_totales.setter
    def bloqueos_totales(self, value):
        self._bloqueos_totales = value

    @porcentaje_tiros_de_campo.setter
    def porcentaje_tiros_de_campo(self, value):
        self._porcentaje_tiros_de_campo = value

    @porcentaje_tiros_libres.setter
    def porcentaje_tiros_libres(self, value):
        self._porcentaje_tiros_libres = value

    @porcentaje_tiros_triples.setter
    def porcentaje_tiros_triples(self, value):
        self._porcentaje_tiros_triples = value


# Clase Jugador
class Jugador:
    def __init__(self, nombre, posicion, logros, estadisticas):
        self._nombre = nombre
        self._posicion = posicion
        self._logros = logros
        self._estadisticas = estadisticas

    # Getters
    @property
    def nombre(self):
        return self._nombre

    @property
    def posicion(self):
        return self._posicion

    @property
    def logros(self):
        return self._logros

    @property
    def estadisticas(self):
        return self._estadisticas

    # Setters
    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @posicion.setter
    def posicion(self, value):
        self._posicion = value

    @logros.setter
    def logros(self, value):
        self._logros = value

    @estadisticas.setter
    def estadisticas(self, value):
        self._estadisticas = value


# Clase Equipo
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
