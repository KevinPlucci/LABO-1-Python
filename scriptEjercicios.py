import os

# Especifica la cantidad de archivos que deseas crear
num_archivos = 20

# Obtiene el directorio actual
directorio_actual = os.getcwd()

# Loop para crear los archivos enumerados
for i in range(1, num_archivos + 1):
    nombre_archivo = f"eje{i}.py"
    ruta_completa = os.path.join(directorio_actual, nombre_archivo)

    # Contenido del archivo (puedes personalizarlo)
    contenido = f"# Este es el archivo {nombre_archivo}\n\nprint('Hola desde {nombre_archivo}')\n"

    # Crea el archivo y escribe el contenido
    with open(ruta_completa, "w") as archivo:
        archivo.write(contenido)

    print(f"Archivo {nombre_archivo} creado en {directorio_actual}")
