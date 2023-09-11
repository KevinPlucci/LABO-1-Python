# Escribir una función que reciba dos string (nombre y apellido) y devuelva un diccionario con el nombre y apellido, eliminando los espacios del comienzo y el final y colocando la primer letra en mayúscula


def formatear_nombre_apellido(nombre, apellido):
    # Eliminar espacios en blanco al comienzo y al final y convertir la primera letra a mayúscula
    nombre_formateado = nombre.strip().capitalize()
    apellido_formateado = apellido.strip().capitalize()

    # Crear un diccionario con el nombre y el apellido formateados
    resultado = {"nombre": nombre_formateado, "apellido": apellido_formateado}

    return resultado


# Ejemplo de uso
nombre = "   juan   "
apellido = "   perez   "
resultado = formatear_nombre_apellido(nombre, apellido)
print(resultado)
