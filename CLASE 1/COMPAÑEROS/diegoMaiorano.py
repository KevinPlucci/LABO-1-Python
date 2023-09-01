import random

# Lista de opciones
lista_opciones = ["Vacuna", "Virus", "Datos"]

# Función para determinar el ganador de una ronda
def determinar_ganador(opcion_jugador, opcion_computadora):
    if opcion_jugador == "Vacuna" and opcion_computadora == "Virus":
        return "Jugador"
    elif opcion_jugador == "Virus" and opcion_computadora == "Datos":
        return "Jugador"
    elif opcion_jugador == "Datos" and opcion_computadora == "Vacuna":
        return "Jugador"
    elif opcion_jugador == opcion_computadora:
        return "Empate"
    else:
        return "Computadora"

# Variables
ganador_partida = None
rondas_para_ganar_partida = 3
victorias_jugador = 0
victorias_computadora = 0

while True:
    if victorias_jugador == rondas_para_ganar_partida:
        ganador_partida = "Jugador"
        break
    elif victorias_computadora == rondas_para_ganar_partida:
        ganador_partida = "Computadora"
        break

    opcion_computadora = random.choice(lista_opciones)
    opcion_jugador = input(
        "Ingresa una opción [Vacuna-Virus-Datos]. Si no es correcta, deberás ingresar de nuevo.\n"
    )

    if opcion_jugador in lista_opciones:
        ganador = determinar_ganador(opcion_jugador, opcion_computadora)

        print("Elección de la computadora:", opcion_computadora)

        if ganador == "Jugador":
            print("Gana el jugador.")
            victorias_jugador += 1
        elif ganador == "Computadora":
            print("Gana la computadora.")
            victorias_computadora += 1
        else:
            print("Empate en esta ronda.")

        print(f"Marcador: Jugador {victorias_jugador} - Computadora {victorias_computadora}\n")
    else:
        print("Opción no válida. Inténtalo nuevamente.\n")

if ganador_partida:
    print(f"¡El ganador de la partida es: {ganador_partida}!")
