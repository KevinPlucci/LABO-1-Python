# Dada una cadena de texto, imprimir la cadena al revés.

# Solicitar al usuario que ingrese una cadena de texto
cadena = input("Ingrese una cadena de texto: ")

# Inicializar un índice al final de la cadena
indice = len(cadena) - 1

# Imprimir la cadena al revés
print("Cadena al revés: ", end="")

while indice >= 0:
    print(cadena[indice], end="")
    indice -= 1

print()  # Salto de línea al final para mejorar la presentación
