# Crear una función que reciba un texto y devuelva una la lista de palabras encuentra que comienzan con una vocal


def palabras_que_comienzan_con_vocal(texto):
    # Dividimos el texto en palabras
    palabras = texto.split()

    # Definimos una lista de vocales en minúsculas
    vocales = ["a", "e", "i", "o", "u"]

    # Utilizamos una comprensión de lista para filtrar las palabras que comienzan con una vocal
    palabras_filtradas = [
        palabra for palabra in palabras if palabra.lower()[0] in vocales
    ]

    return palabras_filtradas


# Ejemplo de uso:
texto = "La tecnología de la información ha revolucionado la comunicación en todas sus formas. La digitalización y la automatización de procesos han permitido la optimización de los recursos y la mejora en la eficiencia de los sistemas. La cibernética, la robótica y la inteligencia artificial son algunas de las áreas de la informática que se han desarrollado en las últimas décadas y han transformado la forma en que vivimos y trabajamos. La interconexión de dispositivos y la transmisión de datos en tiempo real han permitido la creación de nuevas industrias y modelos de negocio que antes eran impensables. La educación, la salud, el transporte y la logística son algunos de los sectores que han sido beneficiados por la innovación tecnológica. En conclusión, la tecnología ha generado una revolución en nuestra sociedad que ha llevado a la transformación y evolución de la misma."

resultado = palabras_que_comienzan_con_vocal(texto)
print(resultado)
