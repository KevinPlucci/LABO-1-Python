import random

# Datos de Agumon
agumon_vida = 100
agumon_ataque = 20

# Datos de Gabumon
gabumon_vida = 100
gabumon_ataque = 18


# Función para simular un ataqueG
def ataque(pypet_atacante, pypet_objetivo):
    dano = random.randint(15, 25)
    pypet_objetivo["vida"] -= dano
    print(
        f"{pypet_atacante['nombre']} infligió {dano} puntos de daño a {pypet_objetivo['nombre']}."
    )


# Simulación del combate
while agumon_vida > 0 and gabumon_vida > 0:
    # Turno de Agumon
    ataque(
        {"nombre": "Agumon", "ataque": agumon_ataque},
        {"nombre": "Gabumon", "vida": gabumon_vida},
    )
    if gabumon_vida <= 0:
        print("¡Has derrotado a Gabumon! ¡Eres el vencedor!")
        break

    # Turno de Gabumon
    ataque(
        {"nombre": "Gabumon", "ataque": gabumon_ataque},
        {"nombre": "Agumon", "vida": agumon_vida},
    )
    if agumon_vida <= 0:
        print("¡Gabumon te ha derrotado! ¡Has perdido la batalla!")
        break
