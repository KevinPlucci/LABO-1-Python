# Crear una función que calcule el área de un triángulo. Recibe dos parámetros (base y altura) y devuelve el área.
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area


# Ejemplo de uso
base = 5
altura = 8
area_del_triangulo = calcular_area_triangulo(base, altura)
print(
    f"El área del triángulo con base {base} y altura {altura} es {area_del_triangulo} unidades cuadradas."
)
