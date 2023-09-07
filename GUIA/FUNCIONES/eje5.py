# Crear una función que determine si un número es primo o no. Recibe un parámetro (número) y devuelve True si es primo y False si no lo es.


def es_primo(numero):
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    # Comprobar si el número es divisible por cualquier número en el rango de 2 a la raíz cuadrada del número + 1
    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            return False  # El número es divisible, por lo que no es primo

    return True  # Si no se encontraron divisores, el número es primo


# Ejemplo de uso
numero = 17
resultado = es_primo(numero)
if resultado:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
