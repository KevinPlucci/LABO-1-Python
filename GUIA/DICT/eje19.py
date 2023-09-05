# Crea un diccionario que represente las temperaturas de una ciudad durante una semana, donde las claves son los días de la semana y los valores son las temperaturas correspondientes.
# Calcula la temperatura promedio de la semana.

# Crear un diccionario con temperaturas de una semana
temperaturas_semana = {
    "Lunes": 25,
    "Martes": 28,
    "Miércoles": 27,
    "Jueves": 30,
    "Viernes": 29,
    "Sábado": 31,
    "Domingo": 26,
}

# Calcular la temperatura promedio de la semana
temperaturas = list(temperaturas_semana.values())
temperatura_promedio = sum(temperaturas) / len(temperaturas)

# Mostrar las temperaturas de la semana
print("Temperaturas de la semana:")
for dia, temperatura in temperaturas_semana.items():
    print("{}: {}°C".format(dia, temperatura))

# Mostrar la temperatura promedio
print("\nTemperatura promedio de la semana: {}°C".format(temperatura_promedio))
