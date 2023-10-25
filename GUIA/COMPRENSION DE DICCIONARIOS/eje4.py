"""
Dado el siguiente texto, crear un diccionario donde clave es una letra y cada valor es la cantidad de veces que aparece la letra dentro del texto
zen_python = """
"""
El Zen de Python, por Tim Peters
Bello es mejor que feo.
Explícito es mejor que implícito.
Simple es mejor que complejo.
Complejo es mejor que complicado.
Plano es mejor que anidado.
Disperso es mejor que denso.
La legibilidad cuenta.
Los casos especiales no son tan especiales como para quebrantar las reglas.
Aunque lo práctico le gana a la pureza.
Errores nunca deberían pasar silenciosamente.
A menos que se silencien explícitamente.
Frente a la ambigüedad, evitar la tentación de adivinar.
Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
Aunque esa manera puede no ser obvia en un primer momento a menos que usted sea holandés.
Ahora es mejor que nunca.
Aunque nunca es a menudo mejor que *ahora* mismo.
Si la implementación es difícil de explicar, es una mala idea.
Si la implementación es fácil de explicar, puede que sea una buena idea.
Los espacios de nombres son una gran idea ¡Hagamos más de eso!
"""

zen_python = """
El Zen de Python, por Tim Peters
Bello es mejor que feo.
Explícito es mejor que implícito.
Simple es mejor que complejo.
Complejo es mejor que complicado.
Plano es mejor que anidado.
Disperso es mejor que denso.
La legibilidad cuenta.
Los casos especiales no son tan especiales como para quebrantar las reglas.
Aunque lo práctico le gana a la pureza.
Errores nunca deberían pasar silenciosamente.
A menos que se silencien explícitamente.
Frente a la ambigüedad, evitar la tentación de adivinar.
Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
Aunque esa manera puede no ser obvia en un primer momento a menos que usted sea holandés.
Ahora es mejor que nunca.
Aunque nunca es a menudo mejor que *ahora* mismo.
Si la implementación es difícil de explicar, es una mala idea.
Si la implementación es fácil de explicar, puede que sea una buena idea.
Los espacios de nombres son una gran idea ¡Hagamos más de eso!
"""

# Crear un diccionario para contar las letras
conteo_letras = {}

# Iterar a través del texto y contar las letras
for letra in zen_python:
    if letra.isalpha():  # Verificar si es una letra
        letra = (
            letra.lower()
        )  # Convertir a minúsculas para no distinguir entre mayúsculas y minúsculas
        if letra in conteo_letras:
            conteo_letras[letra] += 1
        else:
            conteo_letras[letra] = 1

# Mostrar el diccionario de conteo
print(conteo_letras)
