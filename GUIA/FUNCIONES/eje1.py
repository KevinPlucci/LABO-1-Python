# <Crear una función que convierta grados Celsius a grados Fahrenheit. Recibe un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.


def celsius_a_fahrenheit(grados_celsius):
    grados_fahrenheit = (grados_celsius * 9 / 5) + 32
    return grados_fahrenheit


# Ejemplo de uso
grados_celsius = 25
grados_fahrenheit = celsius_a_fahrenheit(grados_celsius)
print(
    f"{grados_celsius} grados Celsius son equivalentes a {grados_fahrenheit} grados Fahrenheit."
)
