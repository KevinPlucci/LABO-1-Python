import random

tipos_pypets = ["Vaccine", "Virus", "Data"]
lista_resultados = [" Ganó el usuario.", " Ganó la CPU.", " Tenemos un empate."]
vidas = 3
vidas_max = 5
ganadas = 0
empatadas = 0
perdidas = 0
racha_actual = 0
racha_max = None


print(f"Comienza el juego. Tenes {vidas} vidas.")
while vidas > 0:
    jugador = input("Ingrese el tipo elegido (Vaccine, Virus o Data): ").capitalize()
    if jugador not in tipos_pypets:
        print("Tipo inexistente. Ingrese un tipo valido (Vaccine, Virus o Data).")
        continue
    print(f"Jugador elige: {jugador}")
    opcion_cpu = random.choice(tipos_pypets)
    print(f"La CPU eligió: {opcion_cpu}")
    if jugador == opcion_cpu:
        mensaje = lista_resultados[2]
        empatadas += 1
        racha = False
    elif (
        jugador == tipos_pypets[0]
        and opcion_cpu == tipos_pypets[1]
        or jugador == tipos_pypets[1]
        and opcion_cpu == tipos_pypets[2]
        or jugador == tipos_pypets[2]
        and opcion_cpu == tipos_pypets[0]
    ):
        mensaje = lista_resultados[0]
        vidas += 1
        ganadas += 1
        racha_actual += 1
        if racha == False:
            racha = True
        else:
            break
    else:
        mensaje = lista_resultados[1]
        vidas -= 1
        perdidas += 1
        racha = False
        racha_actual = 0

    if racha_max == None or racha_actual > racha_max:
        racha_max = racha_actual

    print(mensaje)
    print(f"Te quedan {vidas} restantes y tu racha actual es {racha_actual}")
    if vidas == vidas_max:
        break
informe = f"""
El resultado final es:
Partidas ganadas {ganadas}
Partidas perdidas {perdidas}
Partidas empatadas {empatadas}

"""
print(informe)
