"""
Dada una lista de palabras, imprimir la palabra más larga de la lista.
"""

# Definir una lista de palabras (puedes modificarla según tus necesidades)
palabras = ["gato", "perro", "elefante", "rinoceronte", "jirafa"]

# Inicializar una variable para almacenar la palabra más larga
palabra_mas_larga = palabras[
    0
]  # Asumimos que la primera palabra es la más larga inicialmente

# Iterar a través de la lista para encontrar la palabra más larga
for palabra in palabras:
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra

# Imprimir la palabra más larga
print("La palabra más larga de la lista es:", palabra_mas_larga)
