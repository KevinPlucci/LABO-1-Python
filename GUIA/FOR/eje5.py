# Dada una lista de números, imprimir el número más pequeño de la lista.

# Definir una lista de números (puedes modificarla según tus necesidades)
numeros = [25, 10, 45, 30, 60, 5]

# Inicializar una variable para almacenar el número más pequeño
numero_mas_pequeno = numeros[
    0
]  # Asumimos que el primer número es el más pequeño inicialmente

# Iterar a través de la lista para encontrar el número más pequeño
for numero in numeros:
    if numero < numero_mas_pequeno:
        numero_mas_pequeno = numero

# Imprimir el número más pequeño
print("El número más pequeño de la lista es:", numero_mas_pequeno)
