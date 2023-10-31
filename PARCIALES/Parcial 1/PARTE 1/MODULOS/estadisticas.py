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
