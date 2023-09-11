# Escribir una función que tome un nombre y un apellido y devuelva un email en formato "inicial_nombre.apellido@utn-fra.com.ar".


def generar_email(nombre, apellido):
    # Obtener la inicial del nombre en minúsculas
    inicial_nombre = nombre[0].lower()

    # Reemplazar espacios en blanco en el apellido con "_"
    apellido = apellido.replace(" ", "_").lower()

    # Construir el email en el formato deseado
    email = f"{inicial_nombre}_{nombre.lower()}.{apellido}@utn-fra.com.ar"

    return email


# Ejemplo de uso
nombre = "Juan"
apellido = "Pérez"
email = generar_email(nombre, apellido)
print(email)  # Esto imprimirá "j_juan.perez@utn-fra.com.ar"
