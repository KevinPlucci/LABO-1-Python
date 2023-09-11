# Escribir una función que tome una cadena de texto y devuelva solo los caracteres alfabéticos, eliminando cualquier número o símbolo (sólo son válidos letras y espacios), por ejemplo: "H0l4, m4nd0!" -> "Hl mnd”

import re


def caracteres_alfabeticos(texto):
    # Usar una expresión regular para encontrar solo caracteres alfabéticos y espacios
    texto_limpio = re.sub(r"[^a-zA-Z\s]", "", texto)

    return texto_limpio


# Ejemplo de uso
cadena = "H0l4, m4nd0!"
resultado = caracteres_alfabeticos(cadena)
print(resultado)  # Debería imprimir "Hl mnd"
