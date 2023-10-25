"""
Dado una lista de colores y sus valores hexadecimales
colores_hex = {
    "Rojo": "#FF0000",
    "Verde": "#00FF00",
    "Azul": "#0000FF",
    "Amarillo": "#FFFF00",
    "Naranja": "#FFA500",
    "Violeta": "#8A2BE2",
    "Rosa": "#FFC0CB",
    "Gris": "#808080",
    "Cian": "#00FFFF",
    "Marrón": "#A52A2A"
}

Crea un nuevo diccionario donde los códigos hexadecimales sean las claves y los nombres de colores sean los valores.

"""

colores_hex = {
    "Rojo": "#FF0000",
    "Verde": "#00FF00",
    "Azul": "#0000FF",
    "Amarillo": "#FFFF00",
    "Naranja": "#FFA500",
    "Violeta": "#8A2BE2",
    "Rosa": "#FFC0CB",
    "Gris": "#808080",
    "Cian": "#00FFFF",
    "Marrón": "#A52A2A",
}

# Crea un nuevo diccionario con las claves y valores intercambiados
hex_colores = {valor: clave for clave, valor in colores_hex.items()}

print(hex_colores)
