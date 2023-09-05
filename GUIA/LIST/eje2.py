# Crea una lista con 5 números enteros. Luego solicita un nuevo número y reemplaza el tercer elemento de la lista por el número ingresado. Finalmente imprime todos los números

# Crear una lista con 5 números enteros
numeros = [10, 20, 30, 40, 50]

# Solicitar un nuevo número al usuario
nuevo_numero = int(input("Ingrese un nuevo número: "))

# Reemplazar el tercer elemento de la lista con el número ingresado
numeros[2] = nuevo_numero

# Imprimir todos los números
print("La lista de números actualizada es:")
for numero in numeros:
    print(numero)
