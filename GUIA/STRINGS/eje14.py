# Escribir una función que tome una URL y devuelva solo el nombre de dominio, por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..

from urllib.parse import urlparse


def obtener_nombre_de_dominio(url):
    try:
        # Parsear la URL
        parsed_url = urlparse(url)

        # Obtener el nombre de dominio
        dominio = parsed_url.netloc

        # Dividir el dominio en partes usando el punto como separador
        partes_dominio = dominio.split(".")

        # Si el dominio comienza con "www", omitirlo
        if partes_dominio[0] == "www":
            nombre_de_dominio = partes_dominio[1]
        else:
            nombre_de_dominio = partes_dominio[0]

        return nombre_de_dominio
    except:
        return None


# Ejemplo de uso
url = "https://www.ejemplo.com.ar/pagina1"
nombre_de_dominio = obtener_nombre_de_dominio(url)
if nombre_de_dominio:
    print("Nombre de dominio:", nombre_de_dominio)
else:
    print("URL inválida o no se pudo obtener el nombre de dominio.")
