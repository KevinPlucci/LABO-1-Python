# Crea un diccionario que represente una lista de tareas pendientes, donde las claves son las tareas y los valores son "True" si están completadas y "False" si no lo están.
# Solicita al usuario el nombre de una tarea y modifica el valor para marcarla como completada. Imprimir el listado de tareas pendientes

# Crear un diccionario con tareas pendientes
tareas_pendientes = {
    "Hacer la compra": False,
    "Lavar los platos": False,
    "Estudiar para el examen": False,
    "Hacer ejercicio": False,
}

# Mostrar la lista de tareas pendientes
print("Lista de tareas pendientes:")
for tarea, completada in tareas_pendientes.items():
    estado = "Completada" if completada else "Pendiente"
    print("{}: {}".format(tarea, estado))

# Solicitar al usuario el nombre de una tarea completada
tarea_completada = input("Ingrese el nombre de una tarea que ha completado: ")

# Verificar si la tarea existe en el diccionario
if tarea_completada in tareas_pendientes:
    # Marcar la tarea como completada (True)
    tareas_pendientes[tarea_completada] = True
    print("{} ha sido marcada como completada.".format(tarea_completada))
else:
    print(
        "La tarea '{}' no se encuentra en la lista de tareas pendientes.".format(
            tarea_completada
        )
    )

# Mostrar el listado actualizado de tareas pendientes
print("\nLista de tareas pendientes actualizada:")
for tarea, completada in tareas_pendientes.items():
    estado = "Completada" if completada else "Pendiente"
    print("{}: {}".format(tarea, estado))
