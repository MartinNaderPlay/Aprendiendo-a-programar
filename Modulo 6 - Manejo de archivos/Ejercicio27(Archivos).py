# Leer el archivo del ejercicio anterior y mostrar los datos

import json

with open("nombre_edad.json", "r", encoding="utf-8") as f:
    contenido = f.readlines()

for dato in contenido:
    print(dato.strip())