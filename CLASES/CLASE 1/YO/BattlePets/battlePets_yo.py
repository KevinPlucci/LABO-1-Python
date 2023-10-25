import random

# Datos de Agumon
agumon = {"nombre": "Agumon", "vida": 100, "ataque": 20}

# Datos de Gabumon
gabumon = {"nombre": "Gabumon", "vida": 100, "ataque": 18}


# Función para simular un ataque
def ataque(atacante, defensor):
    dano = random.randint(15, 25)
    defensor["vida"] -= dano
    if defensor["vida"] < 0:
        defensor["vida"] = 0
    print(
        f"{atacante['nombre']} infligió {dano} puntos de daño a {defensor['nombre']} (Vida restante: {defensor['vida']})."
    )


# Simulación del combate
while agumon["vida"] > 0 and gabumon["vida"] > 0:
    # Turno de Agumon
    ataque(agumon, gabumon)
    if gabumon["vida"] <= 0:
        print("¡Has derrotado a Gabumon! ¡Eres el vencedor!")
        break

    # Turno de Gabumon
    ataque(gabumon, agumon)
    if agumon["vida"] <= 0:
        print("¡Gabumon te ha derrotado! ¡Has perdido la batalla!")
        break
