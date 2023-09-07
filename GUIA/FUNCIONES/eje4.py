# Crear una función que calcule el promedio de edad de un grupo de personas. Recibe una lista de edades y devuelve el promedio.


def calcular_promedio_edad(edades):
    if len(edades) == 0:
        return 0  # Evitar la división por cero si la lista está vacía
    suma_edades = sum(edades)
    promedio = suma_edades / len(edades)
    return promedio


# Ejemplo de uso
edades = [30, 25, 40, 22, 35]
promedio_edad = calcular_promedio_edad(edades)
print(f"El promedio de edad es de {promedio_edad:.2f} años.")
