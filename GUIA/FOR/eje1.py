# Definir una lista de números (puedes modificarla según tus necesidades)
numeros = [25, 10, 45, 30, 60, 5]

# Inicializar una variable para almacenar el número más grande
numero_mas_grande = None

# Iterar a través de la lista para encontrar el número más grande
for numero in numeros:
    if numero_mas_grande is None or numero > numero_mas_grande:
        numero_mas_grande = numero

# Imprimir el número más grande
print("El número más grande de la lista es:", numero_mas_grande)
