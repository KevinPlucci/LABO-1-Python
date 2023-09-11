# Crear una función llamada obtener_oraciones que reciba como parámetro un string y que devuelva una lista con las oraciones (delimitadores, ‘.’, ‘!’, ‘?’). Ejemplo de texto:
# texto = "¿Bello es mejor que feo? Explícito es mejor que implícito. Simple es mejor que complejo. Complejo es mejor que complicado. Plano es mejor que anidado.
# Espaciado es mejor que denso. La legibilidad es importante. Los casos especiales no son lo suficientemente especiales como para romper las reglas. Sin embargo la practicidad le gana a la pureza.
# Los errores nunca deberían pasar silenciosamente. A menos que se silencien explícitamente. Frente a la ambigüedad, evitar la tentación de adivinar.
# Debería haber una, y preferiblemente solo una, manera obvia de hacerlo. A pesar de que eso no sea obvio al principio a menos que seas Holandés. Ahora es mejor que nunca.
# A pesar de que nunca es muchas veces mejor que *ahora* mismo. Si la implementación es difícil de explicar, es una mala idea. Si la implementación es fácil de explicar, puede que sea una buena idea.
# Los espacios de nombres son una gran idea, ¡tengamos más de esos!"

import re


def obtener_oraciones(texto):
    # Utilizamos una expresión regular para dividir el texto en oraciones
    # La expresión regular busca puntos '.', exclamaciones '!' y signos de interrogación '?'
    oraciones = re.split(r"[.!?]", texto)

    # Eliminamos las oraciones vacías y eliminamos los espacios en blanco al principio y al final de cada oración
    oraciones_limpia = [oracion.strip() for oracion in oraciones if oracion.strip()]

    return oraciones_limpia


# Ejemplo de uso:
texto = "¿Bello es mejor que feo? Explícito es mejor que implícito. Simple es mejor que complejo. Complejo es mejor que complicado. Plano es mejor que anidado. Espaciado es mejor que denso. La legibilidad es importante. Los casos especiales no son lo suficientemente especiales como para romper las reglas. Sin embargo la practicidad le gana a la pureza. Los errores nunca deberían pasar silenciosamente. A menos que se silencien explícitamente. Frente a la ambigüedad, evitar la tentación de adivinar. Debería haber una, y preferiblemente solo una, manera obvia de hacerlo. A pesar de que eso no sea obvio al principio a menos que seas Holandés. Ahora es mejor que nunca. A pesar de que nunca es muchas veces mejor que *ahora* mismo. Si la implementación es difícil de explicar, es una mala idea. Si la implementación es fácil de explicar, puede que sea una buena idea. Los espacios de nombres son una gran idea, ¡tengamos más de esos!"

resultado = obtener_oraciones(texto)
for oracion in resultado:
    print(oracion)
