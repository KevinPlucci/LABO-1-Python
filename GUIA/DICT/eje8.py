# Crea un diccionario que represente las edades de varias personas, donde las claves son los nombres de las personas y los valores son sus edades. Imprime la edad de la persona más joven.

# Crear el diccionario de edades
edades = {"Juan": 25, "María": 30, "Pedro": 22, "Ana": 28, "Luis": 19}

# Encontrar la edad de la persona más joven
persona_mas_joven = min(edades, key=edades.get)
edad_mas_joven = edades[persona_mas_joven]

# Imprimir la edad de la persona más joven
print(f"La persona más joven es {persona_mas_joven} y tiene {edad_mas_joven} años.")
