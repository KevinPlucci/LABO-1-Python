# LISTAS

lista_valores = [1, 33, 12, -12]
print(lista_valores[1])  # 33
lista_valores[1] = 22
print(lista_valores[1])  # 22

lista_valores.append(99)
print(lista_valores[1])  # 99

for valor in lista_valores:
    print(valor)

for indice in range(len(lista_valores)):
    print(lista_valores[indice])

cantidad_elementos_lista = len(lista_valores)
for indice in range(cantidad_elementos_lista):
    print(lista_valores[indice])
