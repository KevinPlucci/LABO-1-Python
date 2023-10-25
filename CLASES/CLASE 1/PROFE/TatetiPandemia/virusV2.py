"""
    
"""
import random

opciones = ["Vaccine", "Virus", "Data"]
lista_mensajes = ["Gano el usuario", "gano la maquina", "Hay un empate!"]

while True:
    jugador = input("ingrese opcion: ").capitalize()
    if jugador not in opciones:
        print("opcion no valida, vuelve a ingresar opcion")
        continue
    maquina = random.choice(opciones)
    print(f"opcion elegida por la maquina:{maquina}")
    if jugador == maquina:
        mensaje = lista_mensajes[2]
    elif (
        jugador == opciones[0]
        and maquina == opciones[1]
        or jugador == opciones[1]
        and maquina == opciones[2]
        or jugador == opciones[2]
        and maquina == opciones[0]
    ):
        mensaje = lista_mensajes[0]
    else:
        mensaje = lista_mensajes[1]
    print(mensaje)

    continuar = input("Desea continua? s/n: ").lower()
    while continuar != "s" and continuar != "n":
        continuar = input(
            "la opcion ingresada no es correcta, vuelve a ingresar s/n: "
        ).lower()

    if continuar == "n":
        break
