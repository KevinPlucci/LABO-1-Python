# Dada una cadena de texto, imprimir la cantidad de veces que aparece una letra específica en la cadena.


# Pedir al usuario que ingrese una cadena de texto
cadena = input("Ingrese una cadena de texto: ")

# Pedir al usuario que ingrese la letra que desea contar
letra = input("Ingrese la letra que desea contar: ")

# Inicializar una variable para contar la letra
cantidad_de_letra = 0

# Inicializar un índice para recorrer la cadena
indice = 0

# Utilizar un bucle while para contar la letra en la cadena
while indice < len(cadena):
    if cadena[indice] == letra:
        cantidad_de_letra += 1
    indice += 1

# Imprimir la cantidad de veces que aparece la letra
print(f"La letra '{letra}' aparece {cantidad_de_letra} veces en la cadena.")
