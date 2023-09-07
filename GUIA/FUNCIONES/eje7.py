# Crear una función que calcule el máximo común divisor de dos números. Recibe dos parámetros (números) y devuelve el máximo común divisor.


def calcular_mcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Ejemplo de uso
numero1 = 48
numero2 = 18
mcd = calcular_mcd(numero1, numero2)
print(f"El máximo común divisor de {numero1} y {numero2} es {mcd}.")
