# Crear una función llamada validar_ip que reciba un string como parámetro y verifique si se trata de una dirección IP v4 válida, en caso de serlo retornar True de lo contrario retornar False.
# Se considera una dirección IP válida si tiene el formato xxx.xxx.xxx.xxx, donde xxx es un número entero entre 0 y 255.

import re


def validar_ip(ip):
    # Usamos una expresión regular para verificar el formato de la dirección IP.
    patron_ip = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

    # Comprobamos si la cadena coincide con el patrón de dirección IP.
    match = re.match(patron_ip, ip)

    if match:
        # Si coincide con el patrón, obtenemos los grupos de números.
        grupos = match.groups()
        for grupo in grupos:
            # Convertimos cada grupo en un número entero.
            numero = int(grupo)
            # Verificamos si el número está en el rango válido (0-255).
            if numero < 0 or numero > 255:
                return False
        return True
    else:
        return False


# Ejemplo de uso
direccion_ip = "192.168.0.1"  # Cambia esto a la dirección IP que desees verificar
if validar_ip(direccion_ip):
    print("La dirección IP es válida.")
else:
    print("La dirección IP no es válida.")
