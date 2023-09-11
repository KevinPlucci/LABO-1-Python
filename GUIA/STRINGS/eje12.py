# Escribir una función que tome un número de tarjeta de crédito como input, verificar que todos los caracteres sean numéricos y devolver los últimos cuatro dígitos y los primeros dígitos como asteriscos,
# por ejemplo: "**** **** **** 1234".


def ocultar_tarjeta_credito(numero_tarjeta):
    # Verificar que todos los caracteres sean numéricos
    if numero_tarjeta.isdigit() and len(numero_tarjeta) == 16:
        # Obtener los últimos cuatro dígitos
        ultimos_cuatro = numero_tarjeta[-4:]

        # Ocultar los primeros dígitos con asteriscos y agregar espacios
        asteriscos = "*" * 12
        tarjeta_oculta = f"{'*'*4} {'*'*4} {'*'*4} {ultimos_cuatro}"

        return tarjeta_oculta
    else:
        return "Número de tarjeta inválido"


# Ejemplo de uso
numero_tarjeta = "1234567890123456"  # Reemplaza esto con tu número de tarjeta
resultado = ocultar_tarjeta_credito(numero_tarjeta)
print(resultado)  # Esto imprimirá "**** **** **** 3456"
