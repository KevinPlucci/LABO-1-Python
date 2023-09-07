# Crear una función que calcule el descuento aplicado a un producto. Recibe dos parámetros (precio original y precio con descuento) y devuelve el porcentaje de descuento aplicado.


def calcular_porcentaje_descuento(precio_original, precio_con_descuento):
    descuento = precio_original - precio_con_descuento
    porcentaje_descuento = (descuento / precio_original) * 100
    return porcentaje_descuento


# Ejemplo de uso
precio_original = 100
precio_con_descuento = 80
porcentaje_descuento = calcular_porcentaje_descuento(
    precio_original, precio_con_descuento
)
print(f"El porcentaje de descuento aplicado es del {porcentaje_descuento:.2f}%.")
