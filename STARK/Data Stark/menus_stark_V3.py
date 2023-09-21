from typing import List, Dict


def stark_normalizar_datos(lista_heroes: List[Dict]) -> None:
    if not lista_heroes:
        print("Error: Lista de héroes vacía")
        return

    for heroe in lista_heroes:
        for key, value in heroe.items():
            if key in ["altura", "peso", "fuerza"]:
                try:
                    heroe[key] = float(value)
                except ValueError:
                    pass
    print("Datos normalizados")


def obtener_nombre(heroe: Dict) -> str:
    return f"Nombre: {heroe['nombre']}"


def imprimir_dato(dato: str) -> None:
    print(dato)


def stark_imprimir_nombres_heroes(lista_heroes: List[Dict]) -> int:
    if not lista_heroes:
        return -1

    for heroe in lista_heroes:
        imprimir_dato(obtener_nombre(heroe))
    return 0


def obtener_nombre_y_dato(heroe: Dict, key: str) -> str:
    return f"Nombre: {heroe['nombre']} | {key}: {heroe.get(key, 'Dato no encontrado')}"


def stark_imprimir_nombres_alturas(lista_heroes: List[Dict]) -> int:
    if not lista_heroes:
        return -1

    for heroe in lista_heroes:
        imprimir_dato(obtener_nombre_y_dato(heroe, "altura"))
    return 0


def calcular_max(lista_heroes: List[Dict], key: str) -> Dict:
    if not lista_heroes:
        return {}

    max_hero = max(lista_heroes, key=lambda x: x.get(key, 0))
    return max_hero


def calcular_min(lista_heroes: List[Dict], key: str) -> Dict:
    if not lista_heroes:
        return {}

    min_hero = min(lista_heroes, key=lambda x: x.get(key, 0))
    return min_hero


def calcular_max_min_dato(
    lista_heroes: List[Dict], tipo_calculo: str, key: str
) -> Dict:
    if tipo_calculo == "maximo":
        return calcular_max(lista_heroes, key)
    elif tipo_calculo == "minimo":
        return calcular_min(lista_heroes, key)
    else:
        return {}


def stark_calcular_imprimir_heroe(
    lista_heroes: List[Dict], tipo_calculo: str, key: str
) -> int:
    if not lista_heroes:
        return -1

    heroe = calcular_max_min_dato(lista_heroes, tipo_calculo, key)
    if heroe:
        dato = heroe.get(key, "Dato no encontrado")
        imprimir_dato(
            f"{tipo_calculo.capitalize()} {key}: {obtener_nombre_y_dato(heroe, key)}"
        )
    return 0


def sumar_dato_heroe(lista_heroes: List[Dict], key: str) -> float:
    suma = 0
    for heroe in lista_heroes:
        if isinstance(heroe, dict) and key in heroe:
            suma += heroe[key]
    return suma


def dividir(dividendo: float, divisor: float) -> float:
    if divisor == 0:
        return 0
    return dividendo / divisor


def calcular_promedio(lista_heroes: List[Dict], key: str) -> float:
    suma = sumar_dato_heroe(lista_heroes, key)
    cantidad_heroes = len(
        [heroe for heroe in lista_heroes if isinstance(heroe, dict) and key in heroe]
    )
    if cantidad_heroes == 0:
        return 0
    return dividir(suma, cantidad_heroes)


def stark_calcular_imprimir_promedio_altura(lista_heroes: List[Dict]) -> int:
    if not lista_heroes:
        return -1

    promedio_altura = calcular_promedio(lista_heroes, "altura")
    imprimir_dato(f"Promedio altura: {promedio_altura:.2f}")
    return 0


def imprimir_menu() -> None:
    menu = """
    Menú:
    1. Imprimir nombres de héroes
    2. Imprimir nombres y alturas
    3. Calcular e imprimir el héroe con el máximo dato
    4. Calcular e imprimir el héroe con el mínimo dato
    5. Calcular e imprimir el promedio de alturas
    6. Salir
    """
    imprimir_dato(menu)


def validar_entero(numero: str) -> bool:
    return numero.isdigit()


def stark_menu_principal(lista_heroes: List[Dict]) -> int:
    while True:
        imprimir_menu()
        opcion = input("Ingrese el número de la opción deseada: ")
        if validar_entero(opcion):
            opcion = int(opcion)
            if opcion == 1:
                stark_imprimir_nombres_heroes(lista_heroes)
            elif opcion == 2:
                stark_imprimir_nombres_alturas(lista_heroes)
            elif opcion == 3:
                stark_calcular_imprimir_heroe(lista_heroes, "maximo", "fuerza")
            elif opcion == 4:
                stark_calcular_imprimir_heroe(lista_heroes, "minimo", "fuerza")
            elif opcion == 5:
                stark_calcular_imprimir_promedio_altura(lista_heroes)
            elif opcion == 6:
                print("¡Hasta luego!")
                return 0
            else:
                print("Opción no válida. Intente nuevamente.")
        else:
            print("Opción no válida. Intente nuevamente.")


def stark_marvel_app(lista_heroes: List[Dict]) -> None:
    print("Bienvenido a Stark Marvel App")
    stark_menu_principal(lista_heroes)


# Uso de las funciones
if __name__ == "__main__":
    from data_stark import lista_personajes

    stark_normalizar_datos(lista_personajes)
    stark_marvel_app(lista_personajes)
