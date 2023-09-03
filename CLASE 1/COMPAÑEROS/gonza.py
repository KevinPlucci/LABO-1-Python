nota_ingresada = input("Ingresa tu nota wacho: ")

while not nota_ingresada.isdigit():
    nota_ingresada = input("Ingrese una nota valida boludin: ")

    nota = int(nota_ingresada)
    print(f"La nota ingresada fue: {nota}")
