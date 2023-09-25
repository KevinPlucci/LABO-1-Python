lista_buscar_reemplazar = [("Hola", "Hello"), ("Uno", "One"), ("Si", "Yes")]

texto = "*Hola el numero a ser remplazado es el Uno Si y solo Si es ....."

print(texto.split("*"))

texto = "Hola Mundo"

for buscar, reemplazar in lista_buscar_reemplazar:
    texto = texto.replace(buscar, reemplazar)

print(texto)

lista = ["Hola", "Mundo", "Pepe", "Pepe", "Uno"]
texto = " "

print(texto.join(lista))
