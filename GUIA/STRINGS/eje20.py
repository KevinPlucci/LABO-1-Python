# Escribir una función que tome una lista de direcciones de correo electrónico y las una en una sola cadena separada por punto y coma,
# por ejemplo: ["juan@gmail.com", "maria@hotmail.com"] -> "juan@gmail.com;maria@hotmail.com".


def unir_direcciones_de_correo(correos):
    # Usar el método join() para unir los correos con punto y coma
    cadena_unida = ";".join(correos)

    return cadena_unida


# Ejemplo de uso
direcciones_de_correo = ["juan@gmail.com", "maria@hotmail.com"]
cadena_unida = unir_direcciones_de_correo(direcciones_de_correo)
print(cadena_unida)  # Debería imprimir "juan@gmail.com;maria@hotmail.com"
