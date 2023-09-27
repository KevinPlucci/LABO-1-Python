def formatear_puntaje(puntaje) -> str:
    # Asegurarse de que el puntaje sea un número entero
    puntaje = int(puntaje)

    # Formatear el puntaje con dos ceros adelante
    return f"{puntaje:04}"


def formatear_nombre_jugador(nombre: str) -> str:
    # Eliminar espacios en blanco y convertir a mayúsculas
    nombre_formateado = nombre.strip().upper()
    # Truncar el nombre a un máximo de 7 caracteres
    return nombre_formateado[:7]
