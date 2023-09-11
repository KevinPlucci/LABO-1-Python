# Crear una función llamada validar_password que reciba un string y verifique si se trata de una contraseña cumple con los requisitos mínimos de seguridad:
# Al menos 8 caracteres
# Al menos una letra mayúscula y una letra minúscula
# Un número
# Un carácter especial
# En caso de no cumplir con alguno de los requisitos, imprimir un mensaje informando cual no se cumplio

import re


def validar_password(password):
    # Verificar la longitud mínima de 8 caracteres
    if len(password) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return False

    # Verificar al menos una letra mayúscula
    if not re.search(r"[A-Z]", password):
        print("La contraseña debe contener al menos una letra mayúscula.")
        return False

    # Verificar al menos una letra minúscula
    if not re.search(r"[a-z]", password):
        print("La contraseña debe contener al menos una letra minúscula.")
        return False

    # Verificar al menos un número
    if not re.search(r"[0-9]", password):
        print("La contraseña debe contener al menos un número.")
        return False

    # Verificar al menos un carácter especial
    if not re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\|/]", password):
        print("La contraseña debe contener al menos un carácter especial.")
        return False

    # Si se cumplen todos los requisitos, la contraseña es válida
    return True


# Ejemplo de uso
contrasena = "P@ssw0rd"  # Cambia esto a la contraseña que desees verificar
if validar_password(contrasena):
    print("La contraseña es válida.")
else:
    print("La contraseña no es válida.")
