"""
Dado un diccionario de estudiantes y sus calificaciones:
notas = { "Ana": 8, "Juan": 7, "María": 9, "Carlos": 6, "Luisa": 5, "Pedro": 10, "Sofía": 8, "Pablo": 6, "Laura": 9, "Diego": 7 }
Crea un nuevo diccionario donde las calificaciones donde solo se encuentren los alumnos que sacaron nota mayor o igual a 5.
"""

notas = {
    "Ana": 8,
    "Juan": 7,
    "María": 9,
    "Carlos": 6,
    "Luisa": 5,
    "Pedro": 10,
    "Sofía": 8,
    "Pablo": 6,
    "Laura": 9,
    "Diego": 7,
}

notas_aprobados = {alumno: nota for alumno, nota in notas.items() if nota >= 5}

print(notas_aprobados)
