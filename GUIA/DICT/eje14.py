# Crear un diccionario con nombres de jugadores y sus puntajes
jugadores = {"Juan": 1000, "María": 850, "Pedro": 1200, "Ana": 950}

# Mostrar la lista de jugadores y sus puntajes
print("Lista de jugadores y sus puntajes:")
for nombre, puntaje in jugadores.items():
    print("{}: {}".format(nombre, puntaje))

# Pedir al usuario el nombre del jugador y el nuevo puntaje
nombre_jugador = input("Ingrese el nombre del jugador cuyo puntaje desea actualizar: ")
nuevo_puntaje = int(input("Ingrese el nuevo puntaje para {}: ".format(nombre_jugador)))

# Verificar si el jugador existe en el diccionario
if nombre_jugador in jugadores:
    # Actualizar el puntaje del jugador
    jugadores[nombre_jugador] = nuevo_puntaje
    print(
        "El puntaje de {} ha sido actualizado a {}".format(
            nombre_jugador, nuevo_puntaje
        )
    )
else:
    print("El jugador '{}' no existe en la lista.".format(nombre_jugador))

# Mostrar la lista actualizada de jugadores y sus puntajes
print("\nLista de jugadores actualizada:")
for nombre, puntaje in jugadores.items():
    print("{}: {}".format(nombre, puntaje))
