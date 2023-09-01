"""
Escribir un programa que le pida al usuario que ingrese una letra, y luego imprima 
"Es una vocal" si la letra es una vocal (a, e, i, o, u), o "Es una consonante" si la letra es una consonante.
"""

# Solicitar al usuario que ingrese una letra
letra = input("Ingrese una letra: ")

# Verificar si la letra es una vocal o una consonante
if letra.lower() in ("a", "e", "i", "o", "u"):
    print("Es una vocal")
else:
    print("Es una consonante")
