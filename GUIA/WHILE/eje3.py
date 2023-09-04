# Dada una cadena de texto, imprimir cada uno de los caracteres en la cadena.

# Cadena de texto
cadena = "Hola, mundo!"

# Inicializar un índice para recorrer la cadena
indice = 0

# Imprimir cada uno de los caracteres en la cadena
print("Caracteres en la cadena:")

while indice < len(cadena):
    caracter = cadena[indice]
    print(caracter)
    indice += 1
