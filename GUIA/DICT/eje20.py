# Crea un diccionario que represente los asientos de un avión, donde las claves son los números de asientos y los valores son "True" si están ocupados y "False" si no lo están.
# Solicita al usuario un número de asiento y modifica su valor para marcarlo como ocupado. Luego imprimí la lista de asientos libres

# Crear un diccionario con asientos del avión
asientos_avion = {
    "1A": False,
    "1B": False,
    "2A": False,
    "2B": False,
    "3A": False,
    "3B": False,
    "4A": False,
    "4B": False,
    "5A": False,
    "5B": False,
}

# Mostrar la lista de asientos disponibles
print("Lista de asientos disponibles:")
for asiento, ocupado in asientos_avion.items():
    if not ocupado:
        print(asiento)

# Solicitar al usuario un número de asiento
asiento_ocupado = input(
    "Ingrese el número de asiento que desea ocupar (por ejemplo, 1A): "
)

# Verificar si el asiento existe en el diccionario
if asiento_ocupado in asientos_avion:
    # Marcar el asiento como ocupado (True)
    asientos_avion[asiento_ocupado] = True
    print("El asiento {} ha sido marcado como ocupado.".format(asiento_ocupado))
else:
    print("El asiento {} no existe en el avión.".format(asiento_ocupado))

# Mostrar la lista de asientos libres
print("\nLista de asientos libres:")
for asiento, ocupado in asientos_avion.items():
    if not ocupado:
        print(asiento)
