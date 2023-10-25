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

import json


def cargar_heroes():
    with open("data_stark.json", "r") as file:
        data = json.load(file)
    return data["heroes"]


def listar_primeros_n_heroes(heroes, n):
    return heroes[:n]


def ordenar_heroes_por_altura(heroes, ascendente=True):
    return sorted(heroes, key=lambda x: x["altura"], reverse=not ascendente)


def ordenar_heroes_por_fuerza(heroes, ascendente=True):
    return sorted(heroes, key=lambda x: x["fuerza"], reverse=not ascendente)


def buscar_heroes_por_inteligencia(heroes, inteligencia):
    return [hero for hero in heroes if hero["inteligencia"] == inteligencia]


def exportar_heroes_a_csv(heroes, clave, ascendente=True):
    heroes_ordenados = sorted(heroes, key=lambda x: x[clave], reverse=not ascendente)
    with open("heroes.csv", "w") as file:
        for hero in heroes_ordenados:
            file.write(
                f"{hero['nombre']},{hero['identidad']},{hero['altura']},{hero['peso']},{hero['fuerza']},{hero['inteligencia']}\n"
            )
