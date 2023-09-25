lista_de_numeros = [0, 1, 2, 3]  # lista_numeros = list(range(4))

for numero in lista_de_numeros:
    print(numero)

for numero in range(12):
    print(numero)

lista_de_nombres = ["LIO", "EMA", "VERO"]
for nombre in lista_de_nombres:
    print(nombre)

lista_de_nombres = ["LIO", "EMA", "VERO"]
for indice in range(10):
    if lista_de_nombres[indice] == "EMA":
        break  # continue
    print(lista_de_nombres[indice])

lista_de_numeros_texto = []
for indice in range(10):
    numero_texto = input("Numero: ")
    if numero_texto == "EXIT":
        break
    lista_de_numeros_texto.append(numero_texto)

while True:
    numero_texto = input("Numero:")
    if numero_texto == 14:
        break
    print(numero_texto)
