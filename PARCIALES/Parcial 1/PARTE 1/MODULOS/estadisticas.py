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
        """
        Inicializa una instancia de la clase Estadisticas con valores iniciales o por defecto.

        :param temporadas: El número de temporadas jugadas.
        :param puntos_totales: La cantidad total de puntos anotados.
        :param promedio_puntos_por_partido: El promedio de puntos por partido.
        :param rebotes_totales: La cantidad total de rebotes.
        :param promedio_rebotes_por_partido: El promedio de rebotes por partido.
        :param asistencias_totales: La cantidad total de asistencias.
        :param promedio_asistencias_por_partido: El promedio de asistencias por partido.
        :param robos_totales: La cantidad total de robos realizados.
        :param bloqueos_totales: La cantidad total de bloqueos realizados.
        :param porcentaje_tiros_de_campo: El porcentaje de tiros de campo exitosos.
        :param porcentaje_tiros_libres: El porcentaje de tiros libres exitosos.
        :param porcentaje_tiros_triples: El porcentaje de tiros triples exitosos.
        """
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
        """
        Obtiene el número de temporadas jugadas.
        """
        return self._temporadas

    @property
    def puntos_totales(self):
        """
        Obtiene la cantidad total de puntos anotados.
        """
        return self._puntos_totales

    @property
    def promedio_puntos_por_partido(self):
        """
        Obtiene el promedio de puntos por partido.
        """
        return self._promedio_puntos_por_partido

    @property
    def rebotes_totales(self):
        """
        Obtiene la cantidad total de rebotes.
        """
        return self._rebotes_totales

    @property
    def promedio_rebotes_por_partido(self):
        """
        Obtiene el promedio de rebotes por partido.
        """
        return self._promedio_rebotes_por_partido

    @property
    def asistencias_totales(self):
        """
        Obtiene la cantidad total de asistencias.
        """
        return self._asistencias_totales

    @property
    def promedio_asistencias_por_partido(self):
        """
        Obtiene el promedio de asistencias por partido.
        """
        return self._promedio_asistencias_por_partido

    @property
    def robos_totales(self):
        """
        Obtiene la cantidad total de robos realizados.
        """
        return self._robos_totales

    @property
    def bloqueos_totales(self):
        """
        Obtiene la cantidad total de bloqueos realizados.
        """
        return self._bloqueos_totales

    @property
    def porcentaje_tiros_de_campo(self):
        """
        Obtiene el porcentaje de tiros de campo exitosos.
        """
        return self._porcentaje_tiros_de_campo

    @property
    def porcentaje_tiros_libres(self):
        """
        Obtiene el porcentaje de tiros libres exitosos.
        """
        return self._porcentaje_tiros_libres

    @property
    def porcentaje_tiros_triples(self):
        """
        Obtiene el porcentaje de tiros triples exitosos.
        """
        return self._porcentaje_tiros_triples

    # Setters
    @temporadas.setter
    def temporadas(self, value):
        """
        Establece el número de temporadas jugadas.

        :param value: El nuevo valor para el número de temporadas jugadas.
        """
        self._temporadas = value

    @puntos_totales.setter
    def puntos_totales(self, value):
        """
        Establece la cantidad total de puntos anotados.

        :param value: El nuevo valor para la cantidad total de puntos anotados.
        """
        self._puntos_totales = value

    @promedio_puntos_por_partido.setter
    def promedio_puntos_por_partido(self, value):
        """
        Establece el promedio de puntos por partido.

        :param value: El nuevo valor para el promedio de puntos por partido.
        """
        self._promedio_puntos_por_partido = value

    @rebotes_totales.setter
    def rebotes_totales(self, value):
        """
        Establece la cantidad total de rebotes.

        :param value: El nuevo valor para la cantidad total de rebotes.
        """
        self._rebotes_totales = value

    @promedio_rebotes_por_partido.setter
    def promedio_rebotes_por_partido(self, value):
        """
        Establece el promedio de rebotes por partido.

        :param value: El nuevo valor para el promedio de rebotes por partido.
        """
        self._promedio_rebotes_por_partido = value

    @asistencias_totales.setter
    def asistencias_totales(self, value):
        """
        Establece la cantidad total de asistencias.

        :param value: El nuevo valor para la cantidad total de asistencias.
        """
        self._asistencias_totales = value

    @promedio_asistencias_por_partido.setter
    def promedio_asistencias_por_partido(self, value):
        """
        Establece el promedio de asistencias por partido.

        :param value: El nuevo valor para el promedio de asistencias por partido.
        """
        self._promedio_asistencias_por_partido = value

    @robos_totales.setter
    def robos_totales(self, value):
        """
        Establece la cantidad total de robos realizados.

        :param value: El nuevo valor para la cantidad total de robos realizados.
        """
        self._robos_totales = value

    @bloqueos_totales.setter
    def bloqueos_totales(self, value):
        """
        Establece la cantidad total de bloqueos realizados.

        :param value: El nuevo valor para la cantidad total de bloqueos realizados.
        """
        self._bloqueos_totales = value

    @porcentaje_tiros_de_campo.setter
    def porcentaje_tiros_de_campo(self, value):
        """
        Establece el porcentaje de tiros de campo exitosos.

        :param value: El nuevo valor para el porcentaje de tiros de campo exitosos.
        """
        self._porcentaje_tiros_de_campo = value

    @porcentaje_tiros_libres.setter
    def porcentaje_tiros_libres(self, value):
        """
        Establece el porcentaje de tiros libres exitosos.

        :param value: El nuevo valor para el porcentaje de tiros libres exitosos.
        """
        self._porcentaje_tiros_libres = value

    @porcentaje_tiros_triples.setter
    def porcentaje_tiros_triples(self, value):
        """
        Establece el porcentaje de tiros triples exitosos.

        :param value: El nuevo valor para el porcentaje de tiros triples exitosos.
        """
        self._porcentaje_tiros_triples = value
