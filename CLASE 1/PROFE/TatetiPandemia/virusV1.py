"""
Ideas

lista con opciones(validar)
evaluar quien gana
funcion input()
condicionales para hacer las comparaciones

Vaccine Virus Data
"""
import random

#variables
lista_de_opciones = ["Vaccine", "Virus", "Data"]
lista_de_mensajes = ["Gano el usuario", "gano la maquina", "Hay un empate!"]
dato_ingresado = None
mensaje = None

while (dato_ingresado != "Vaccine" and dato_ingresado != "Virus" 
       and dato_ingresado != "Data"):
    dato_ingresado = input("ingrese su opcion: ")

print(f"la opcion elegida fue: {dato_ingresado}")

opcion_cpu = random.choice(lista_de_opciones)
print(f"la opcion elegida por la maquina fue: {opcion_cpu}")

match dato_ingresado:
    case "Vaccine":
        if opcion_cpu == "Virus":
            mensaje = lista_de_mensajes[0]
        elif opcion_cpu == "Data":
            mensaje = lista_de_mensajes[1]
        else:
            mensaje = lista_de_mensajes[2]
    case "Virus":
        if opcion_cpu == "Data":
            mensaje = lista_de_mensajes[0]
        elif opcion_cpu == "Vaccine":
            mensaje = lista_de_mensajes[1]
        else:
            mensaje = lista_de_mensajes[2]
    case _:
        if opcion_cpu == "Vaccine":
            mensaje = lista_de_mensajes[0]
        elif opcion_cpu == "Virus":
            mensaje = lista_de_mensajes[1]
        else:
            mensaje = lista_de_mensajes[2]

print(mensaje)
        