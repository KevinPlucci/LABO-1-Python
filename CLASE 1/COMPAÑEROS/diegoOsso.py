import random

tipos_pypets = ["Vaccine", "Virus", "Data"]
lista_resultados = ["Gano el usuario.", "Gano la CPU.", "Tenemos un empate."]
partida = ["si", "no"]

while True:
    jugador = input("Ingrese el tipo elegido(Vaccine, Virus o Data): ").capitalize()
    if jugador not in tipos_pypets:
        print("Tipo inexistente. Ingrese un tipo valido(Vaccine, Virus o Data). ")
        continue
    print(f"Jugador elige:{jugador}")
    opcion_cpu = random.choice(tipos_pypets)
    print(f"La CPU eligio: {opcion_cpu}")
    if jugador == opcion_cpu:
        mensaje = lista_resultados[2]
    elif (
        jugador == tipos_pypets[0]
        and opcion_cpu == tipos_pypets[1]
        or jugador == tipos_pypets[1]
        and opcion_cpu == tipos_pypets[2]
        or jugador == tipos_pypets[2 and opcion_cpu == tipos_pypets[0]]
    ):
        mensaje = lista_resultados[0]
    else:
        mensaje = lista_resultados[1]
    print(mensaje)

    continuar = input("¿Quiere jugar otra partida? si/no: ").lower()
    while continuar not in partida:
        continuar = input("Seleccione una opcion valida(si/no): ")
    if continuar == "no":
        break
