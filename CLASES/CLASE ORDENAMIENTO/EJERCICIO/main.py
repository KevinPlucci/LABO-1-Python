# MIT License
#
# Copyright (c) 2022 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
{
    "nombre": "Deadpool",
    "identidad": "Wade Wilson",
    "altura": 188.0,
    "peso": 95.32,
    "fuerza": 35,
    "inteligencia": "good"
}

1 - Listar los primeros N heroes
2 - Ordenar heroes por altura [Ascendente o Descendente]
3 - Ordenar heroes por fuerza [Ascendente o Descendente]
4 - Buscar heroes por inteligencia [good, average, high] 
5 - Exportar lista Ordenada de heroes ordenada [ASC o DESC] por una clave que decida el usuario a CSV
7 - Salir
"""

import funciones as f


def stark_parcial():
    heroes = list(f.cargar_heroes())

    while True:
        print("1 - Listar los primeros N héroes")
        print("2 - Ordenar héroes por altura [Ascendente o Descendente]")
        print("3 - Ordenar héroes por fuerza [Ascendente o Descendente]")
        print("4 - Buscar héroes por inteligencia [good, average, high]")
        print("5 - Exportar lista ordenada de héroes a CSV")
        print("6 - Salir")

        respuesta = input("Elija una opción: ")

        if respuesta == "1":
            n = int(input("Ingrese el número de héroes a listar:"))
            heroes_n = f.listar_primeros_n_heroes(heroes, n)
            for hero in heroes_n:
                print(hero["nombre"])

        elif respuesta == "2":
            ascendente = input("¿Ordenar ascendente (S/N)? ").strip().lower() == "s"
            heroes_ordenados = f.ordenar_heroes_por_altura(heroes, ascendente)
            for hero in heroes_ordenados:
                print(hero["nombre"])

        elif respuesta == "3":
            ascendente = input("¿Ordenar ascendente (S/N)? ").strip().lower() == "s"
            heroes_ordenados = f.ordenar_heroes_por_fuerza(heroes, ascendente)
            for hero in heroes_ordenados:
                print(hero["nombre"])

        elif respuesta == "4":
            inteligencia = input("Inteligencia (good, average, high): ")
            heroes_inteligencia = f.buscar_heroes_por_inteligencia(heroes, inteligencia)
            for hero in heroes_inteligencia:
                print(hero["nombre"])

        elif respuesta == "5":
            clave = input(
                "Clave de ordenamiento (altura, peso, fuerza, inteligencia): "
            )
            ascendente = input("¿Ordenar ascendente (S/N)? ").strip().lower() == "s"
            f.exportar_heroes_a_csv(heroes, clave, ascendente)
            print("Datos exportados a heroes.csv")

        elif respuesta == "6":
            print("Fin de la ejecución")
            break


if __name__ == "__main__":
    stark_parcial()
