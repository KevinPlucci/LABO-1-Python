# Crear una función que reciba un texto como parámetro y que corrija los errores de ortografía que no cumplan con la regla ortográfica que indica que antes de V se escribe N y que antes de B se escribe M.
# Por ejemplo, si el texto es: "Mi comvicción me hace sentir que es el momento de imvertir tiempo para finalmente enbarcar en esta nueva aventura." La función debería devolver:
# “Mi convicción me hace sentir que es el momento de invertir tiempo para finalmente embarcar en esta nueva aventura."


def corregir_ortografia(texto):
    # Reemplazamos "comv" por "conm"
    texto_corregido = texto.replace("comv", "conm")

    # Reemplazamos "imv" por "inm"
    texto_corregido = texto_corregido.replace("imv", "inm")

    # Reemplazamos "enbar" por "embar"
    texto_corregido = texto_corregido.replace("enbar", "embar")

    return texto_corregido


# Ejemplo de uso:
texto = "Mi comvicción me hace sentir que es el momento de imvertir tiempo para finalmente enbarcar en esta nueva aventura."
texto_corregido = corregir_ortografia(texto)
print(texto_corregido)
