import json
import re
import csv


# Cargar datos desde el archivo JSON
def cargar_datos():
    try:
        with open("data_stark.json", "r") as archivo_json:
            data = json.load(archivo_json)["heroes"]
        return data
    except FileNotFoundError:
        print("El archivo 'data_stark.json' no se encuentra.")
        return None


# Función para listar los primeros N héroes
def listar_primeros_heroes(data, n):
    if n < 1 or n > len(data):
        print("N debe estar en el rango de 1 a", len(data))
        return
    primeros_heroes = data[:n]
    for heroe in primeros_heroes:
        print(heroe["nombre"])


# Función para ordenar y listar héroes por altura
def ordenar_y_listar_por_altura(data, orden):
    heroes_copia = data.copy()
    heroes_copia.sort(key=lambda x: float(x["altura"]), reverse=orden == "desc")
    for heroe in heroes_copia:
        print(f"Nombre: {heroe['nombre']}, Altura: {float(heroe['altura']):.2f}")


# Función para ordenar y listar héroes por fuerza
def ordenar_y_listar_por_fuerza(data, orden):
    heroes_copia = data.copy()
    heroes_copia.sort(key=lambda x: float(x["fuerza"]), reverse=orden == "desc")
    for heroe in heroes_copia:
        print(f"Nombre: {heroe['nombre']}, Fuerza: {float(heroe['fuerza']):.2f}")


# Función para calcular el promedio de una clave numérica
def calcular_promedio(data, clave):
    valores_numericos = [
        float(heroe[clave]) for heroe in data if heroe[clave].isdigit()
    ]
    if not valores_numericos:
        return None
    promedio = sum(valores_numericos) / len(valores_numericos)
    return promedio


# Función para filtrar héroes por condición de superar o no el promedio
def filtrar_por_promedio(data, clave, condicion, mostrar_completo=False):
    if not condicion in ("menor", "mayor"):
        print("Condición no válida. Debe ser 'menor' o 'mayor'.")
        return []

    promedio = calcular_promedio(data, clave)
    if promedio is None:
        print("No hay valores numéricos para calcular el promedio.")
        return []

    filtrados = []
    for heroe in data:
        valor = float(heroe[clave])
        if (condicion == "menor" and valor < promedio) or (
            condicion == "mayor" and valor > promedio
        ):
            filtrados.append(heroe)

    if not filtrados:
        print("No hay héroes que cumplan la condición.")
        return []

    if not mostrar_completo:
        for heroe in filtrados:
            print(f"Nombre: {heroe['nombre']}")  # Imprimir solo el nombre

    return filtrados


# Función para buscar héroes por inteligencia usando RegEx
# Función para buscar héroes por inteligencia usando RegEx
def buscar_por_inteligencia(data, inteligencia):
    patron = re.compile(inteligencia, re.IGNORECASE)
    encontrados = [
        heroe["nombre"] for heroe in data if patron.search(heroe["inteligencia"])
    ]
    return encontrados


# Función para exportar la lista de héroes a un archivo CSV
def exportar_a_csv(data, nombre_archivo):
    if not nombre_archivo.endswith(".csv"):
        nombre_archivo += ".csv"  # Agregar la extensión .csv si no está presente

    with open(nombre_archivo, mode="w", newline="") as archivo_csv:
        campos = data[0].keys()
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
        escritor_csv.writeheader()
        for heroe in data:
            escritor_csv.writerow(heroe)

    print("Datos exportados a", nombre_archivo)


if __name__ == "__main__":
    datos = cargar_datos()
    if datos:
        while True:
            print("\nMenú:")
            print("1. Listar los primeros N héroes")
            print("2. Ordenar y listar héroes por altura")
            print("3. Ordenar y listar héroes por fuerza")
            print("4. Calcular promedio y filtrar por condición")
            print("5. Buscar héroes por inteligencia")
            print("6. Exportar a CSV")
            print("7. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                n = int(input("Ingrese el valor de N: "))
                listar_primeros_heroes(datos, n)
            elif opcion == "2":
                orden = input(
                    "Ingrese 'asc' para ascendente o 'desc' para descendente: "
                )
                ordenar_y_listar_por_altura(datos, orden)
            elif opcion == "3":
                orden = input(
                    "Ingrese 'asc' para ascendente o 'desc' para descendente: "
                )
                ordenar_y_listar_por_fuerza(datos, orden)
            elif opcion == "4":
                clave = input("Ingrese la clave numérica (ejemplo: 'fuerza'): ")
                condicion = input("Ingrese 'menor' o 'mayor' para la condición: ")
                filtrados = filtrar_por_promedio(datos, clave, condicion)
            elif opcion == "5":
                inteligencia = input(
                    "Ingrese el nivel de inteligencia (good, average, high): "
                )
                encontrados = buscar_por_inteligencia(datos, inteligencia)
                for heroe in encontrados:
                    print(heroe)
            elif opcion == "6":
                nombre_archivo = input("Ingrese el nombre del archivo CSV: ")
                exportar_a_csv(datos, nombre_archivo)
                print("Datos exportados a", nombre_archivo)
            elif opcion == "7":
                break
            else:
                print("Opción no válida. Intente de nuevo.")
