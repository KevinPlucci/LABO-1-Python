# Crea un diccionario que represente las notas de un examen de varios estudiantes, donde las claves son los nombres de los estudiantes y los valores son sus notas. Imprime el promedio de las notas.

# Crear el diccionario de notas de los estudiantes
notas = {
    "Estudiante1": 85,
    "Estudiante2": 92,
    "Estudiante3": 78,
    "Estudiante4": 95,
    "Estudiante5": 88,
}

# Calcular el promedio de las notas
total_notas = sum(notas.values())
cantidad_estudiantes = len(notas)
promedio = total_notas / cantidad_estudiantes

# Imprimir el promedio de las notas
print(f"El promedio de las notas es: {promedio:.2f}")
