# Dada una cadena de texto, imprimir la cantidad de vocales en la cadena.

# Cadena de texto
texto = "Hola, cómo estás?"

# Convertir la cadena a minúsculas para simplificar la comparación
texto = texto.lower()

# Inicializar una variable para contar las vocales
contador_vocales = 0

# Inicializar un índice para recorrer la cadena
indice = 0

# Imprimir la cantidad de vocales en la cadena
print("Cantidad de vocales en la cadena:")

while indice < len(texto):
    caracter = texto[indice]
    if caracter in "aeiouáéíóú":
        contador_vocales += 1
    indice += 1

print("Número total de vocales:", contador_vocales)
