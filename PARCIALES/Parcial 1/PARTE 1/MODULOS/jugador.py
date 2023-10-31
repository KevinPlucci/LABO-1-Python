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
