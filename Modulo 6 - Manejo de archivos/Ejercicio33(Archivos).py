# Modificar un dato dentro del json.

import json

with open("contactos_tel.json", "r", encoding="utf-8") as f:
    contenido = json.load(f)

nombre = input("Escriba un nombre para modificar un dato: ")

if nombre in contenido:
    contenido[nombre] = int(input("Escriba el nuevo número: "))
else:
    print("El nombre escrito no pertenece a la lista o está mal escrito")

with open("contactos_tel.json", "w", encoding="utf-8") as f:
    json.dump(contenido, f)