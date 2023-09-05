# Crea un diccionario que represente una lista de tareas por hacer.
# Cada clave del diccionario debe ser el nombre de una tarea y cada valor debe ser su estado (los estados son:  pendiente, en proceso, completada).
# Imprimir todas las tareas seguido de su estado


# Crear el diccionario de tareas por hacer
tareas = {
    "Tarea1": "pendiente",
    "Tarea2": "en proceso",
    "Tarea3": "completada",
    "Tarea4": "pendiente",
    "Tarea5": "en proceso",
}

# Imprimir todas las tareas y sus estados
for tarea, estado in tareas.items():
    print(f"Tarea: {tarea}, Estado: {estado}")
