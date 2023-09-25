texto = input("Ingrese orden")

match texto:
    case "SALTAR":
        print("La orden es..." + texto)
    case "CORRER":
        print("La orden es...{0}".format(texto))
    case other:
        print("La orden es...{0}".format(texto))

if texto == "SALTAR":
    print("La orden es SALTAR...{0}".format(texto))
elif texto == "CORRER":
    print("La orden es CORRER...".format(texto))
else:
    print("La orden es...{0}".format(texto))
