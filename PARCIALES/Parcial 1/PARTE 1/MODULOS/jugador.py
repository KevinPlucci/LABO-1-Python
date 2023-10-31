# Clase Jugador
class Jugador:
    def __init__(self, nombre, posicion, logros, estadisticas):
        """
        Inicializa una instancia de la clase Jugador con los atributos proporcionados.

        :param nombre: El nombre del jugador.
        :param posicion: La posición en la que juega el jugador.
        :param logros: Una lista de logros o premios del jugador.
        :param estadisticas: Un objeto de la clase Estadisticas que contiene las estadísticas del jugador.
        """
        self._nombre = nombre
        self._posicion = posicion
        self._logros = logros
        self._estadisticas = estadisticas

    # Getters
    @property
    def nombre(self):
        """
        Obtiene el nombre del jugador.
        """
        return self._nombre

    @property
    def posicion(self):
        """
        Obtiene la posición en la que juega el jugador.
        """
        return self._posicion

    @property
    def logros(self):
        """
        Obtiene una lista de logros o premios del jugador.
        """
        return self._logros

    @property
    def estadisticas(self):
        """
        Obtiene un objeto de la clase Estadisticas que contiene las estadísticas del jugador.
        """
        return self._estadisticas

    # Setters
    @nombre.setter
    def nombre(self, value):
        """
        Establece el nombre del jugador.

        :param value: El nuevo nombre del jugador.
        """
        self._nombre = value

    @posicion.setter
    def posicion(self, value):
        """
        Establece la posición en la que juega el jugador.

        :param value: La nueva posición del jugador.
        """
        self._posicion = value

    @logros.setter
    def logros(self, value):
        """
        Establece una lista de logros o premios del jugador.

        :param value: La nueva lista de logros o premios del jugador.
        """
        self._logros = value

    @estadisticas.setter
    def estadisticas(self, value):
        """
        Establece un objeto de la clase Estadisticas que contiene las estadísticas del jugador.

        :param value: El nuevo objeto de estadísticas del jugador.
        """
        self._estadisticas = value
