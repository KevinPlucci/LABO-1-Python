# Crea una lista vacía y pide al usuario que ingrese una palabra. Luego, muestra la primera letra de la palabra. Repite este proceso hasta que el usuario ingrese una palabra que comience con la letra "z".

# Crear una lista vacía para almacenar las palabras ingresadas
palabras = []

# Solicitar al usuario que ingrese palabras hasta que ingrese una que comience con "z"
while True:
    palabra = input(
        "Ingrese una palabra (ingrese una palabra que comience con 'z' para finalizar): "
    )
    palabras.append(palabra)

    # Verificar si la palabra comienza con "z" y salir del bucle si es así
    if palabra.startswith("z"):
        break

# Mostrar la primera letra de cada palabra ingresada
for palabra in palabras:
    primera_letra = palabra[0]
    print(f"La primera letra de '{palabra}' es: {primera_letra}")
