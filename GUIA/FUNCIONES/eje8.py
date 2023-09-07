# Crear una función que verifique si un número es par o impar. Recibe un número como parámetro y devuelve True si es par o False si es impar.


def es_par_o_impar(numero):
    if numero % 2 == 0:
        return True  # Es par
    else:
        return False  # Es impar


# Ejemplo de uso
numero = 10
if es_par_o_impar(numero):
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")
