# Crear una función que calcule el área de un círculo. Recibe un parámetro (radio) y devuelve el área del círculo.

import math


def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area


# Ejemplo de uso
radio = 5
area_del_circulo = calcular_area_circulo(radio)
print(
    f"El área del círculo con radio {radio} es {area_del_circulo:.2f} unidades cuadradas."
)
