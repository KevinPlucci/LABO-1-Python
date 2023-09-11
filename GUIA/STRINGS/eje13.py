# Escribir una función que tome un correo electrónico y elimine cualquier carácter después del símbolo @, por ejemplo: "usuario@gmail.com" -> "usuario".


def eliminar_despues_de_arroba(correo):
    # Dividir el correo en dos partes en función del símbolo "@" y tomar la primera parte
    partes = correo.split("@")
    usuario = partes[0]
    return usuario


# Ejemplo de uso
correo = "usuario@gmail.com"
resultado = eliminar_despues_de_arroba(correo)
print(resultado)  # Esto imprimirá "usuario"
