# Crear una función que se llame obtener_direcciones_email que reciba un texto y devuelva una lista con todas las direcciones de email válidas que encuentren en el mismo. Acá dejamos un texto de ejemplo:
# datos = " <Alberto, Cervantes> acervantes@gmx.com <Ana, Jimenez> ajimenez@hotmail.com <Antonio, Castillo> acastillo@gmail.com <Armando, Vega> avega@yahoo.com <Arturo, Arredondo>
# aarredondo@gmail.com <Beatriz, Vargas> bvargas@outlook.com <Berenice, Rios> bribos@yahoo.com <Brenda, Gonzalez> bgonzalez@terra.com <Brian, Hernandez> bhernandez@outlook.com
# <Camila, Reyes> creyes@terra.com <Carlos, Gallegos> cgallegos@gmail.com <Carolina, Alvarado> calvarado@outlook.com <Cesar, Rosales> crosales@terra.com <Christian, Moreno> cmoreno@gmail.com
# <Clara, Serrano> cserrano@yahoo.com <Cristian, Huerta> chuerta@terra.com <Cristina, Ochoa> cochoa@yahoo.com <Dalia, Rivas> drivas@outlook.com <Daniel, Perez> dperez@yahoo.com
# <Daniela, Ruiz> druiz@outlook.com <David, Velasco> dvelasco@gmail.com <Diana, Andrade> dandrade@yahoo.com <Diego, Ortiz> dortiz@terra.com <Eduardo, Vazquez> evazquez@gmail.com
# <Elisa, Castillo> ecastillo@outlook.com <Elizabeth, Cruz> ecruz@yahoo.com <Emmanuel, Pacheco> epacheco@terra.com <Enrique, Fuentes> efuentes@gmail.com <Erika, Cabrera> ecabrera@yahoo.com
# <Erick, Zavala> ezavala@outlook.com <Esmeralda, Valdes> evaldes@gmx.com <Esteban, Montes> emontes@gmail.com <Evelyn, Vera> evera@yahoo.com <Fabian, Rangel> frangel@terra.com <Fatima, De La Cruz>
# fdela@gmx.com <Felipe, Salas> fsalas@outlook.com <Fernanda, Guerrero> fguerrero@gmail.com <Fernando, Olvera> folvera@yahoo.com <Francisco, Hernandez> fhernandez@terra.com <Gabriela, Acosta>
# gacosta@gmail.com <Gael, Maldonado> gmaldonado@outlook.com <Gerardo, Flores> gflores@yahoo.com <Giselle, Alvarado> galvarado@terra.com <Gloria, Tapia> gtapia@gmx.com
# <Gonzalo, Zamora> gzamora@yahoo.com <Graciela, Ochoa> gochoa@outlook.com <Guadalupe, Aguilar> gaguilar@gmail.com <Guillermo, Garza> ggarza@yahoo.com <Gustavo, Mora> gmora@terra.com
# <Heidi, Hernandez> hhernandez@gmx.com <Hector, Barrios> hbarrios@outlook.com <Hugo, Villarreal> hvillarreal@yahoo.com <Ignacio, Soto> isoto@gmail.com <Ingrid, Vidal> ividal@yahoo.com
# <Irma, Garza> igarza@terra.com <Isaac, Palacios> ipalacios@gmail.com <Ivan, Rojas> irojas@yahoo.com

import re


def obtener_direcciones_email(texto):
    # Utilizamos una expresión regular para encontrar direcciones de correo electrónico válidas.
    patron_email = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    # Buscamos todas las coincidencias en el texto.
    direcciones_email = re.findall(patron_email, texto)

    return direcciones_email


# Texto de ejemplo
datos = "<Alberto, Cervantes> acervantes@gmx.com <Ana, Jimenez> ajimenez@hotmail.com <Antonio, Castillo> acastillo@gmail.com <Armando, Vega> avega@yahoo.com <Arturo, Arredondo> aarredondo@gmail.com <Beatriz, Vargas> bvargas@outlook.com <Berenice, Rios> bribos@yahoo.com <Brenda, Gonzalez> bgonzalez@terra.com <Brian, Hernandez> bhernandez@outlook.com <Camila, Reyes> creyes@terra.com <Carlos, Gallegos> cgallegos@gmail.com <Carolina, Alvarado> calvarado@outlook.com <Cesar, Rosales> crosales@terra.com <Christian, Moreno> cmoreno@gmail.com <Clara, Serrano> cserrano@yahoo.com <Cristian, Huerta> chuerta@terra.com <Cristina, Ochoa> cochoa@yahoo.com <Dalia, Rivas> drivas@outlook.com <Daniel, Perez> dperez@yahoo.com <Daniela, Ruiz> druiz@outlook.com <David, Velasco> dvelasco@gmail.com <Diana, Andrade> dandrade@yahoo.com <Diego, Ortiz> dortiz@terra.com <Eduardo, Vazquez> evazquez@gmail.com <Elisa, Castillo> ecastillo@outlook.com <Elizabeth, Cruz> ecruz@yahoo.com <Emmanuel, Pacheco> epacheco@terra.com <Enrique, Fuentes> efuentes@gmail.com <Erika, Cabrera> ecabrera@yahoo.com <Erick, Zavala> ezavala@outlook.com <Esmeralda, Valdes> evaldes@gmx.com <Esteban, Montes> emontes@gmail.com <Evelyn, Vera> evera@yahoo.com <Fabian, Rangel> frangel@terra.com <Fatima, De La Cruz> fdela@gmx.com <Felipe, Salas> fsalas@outlook.com <Fernanda, Guerrero> fguerrero@gmail.com <Fernando, Olvera> folvera@yahoo.com <Francisco, Hernandez> fhernandez@terra.com <Gabriela, Acosta> gacosta@gmail.com <Gael, Maldonado> gmaldonado@outlook.com <Gerardo, Flores> gflores@yahoo.com <Giselle, Alvarado> galvarado@terra.com <Gloria, Tapia> gtapia@gmx.com <Gonzalo, Zamora> gzamora@yahoo.com <Graciela, Ochoa> gochoa@outlook.com <Guadalupe, Aguilar> gaguilar@gmail.com <Guillermo, Garza> ggarza@yahoo.com <Gustavo, Mora> gmora@terra.com <Heidi, Hernandez> hhernandez@gmx.com <Hector, Barrios> hbarrios@outlook.com <Hugo, Villarreal> hvillarreal@yahoo.com <Ignacio, Soto> isoto@gmail.com <Ingrid, Vidal> ividal@yahoo.com <Irma, Garza> igarza@terra.com <Isaac, Palacios> ipalacios@gmail.com <Ivan, Rojas> irojas@yahoo.com <Jacqueline, Fuentes> jfuentes@outlook.com <Jaime, Huerta> jhuerta@yahoo"

# Llama a la función e imprime las direcciones de correo electrónico encontradas
direcciones_encontradas = obtener_direcciones_email(datos)
for direccion in direcciones_encontradas:
    print(direccion)
