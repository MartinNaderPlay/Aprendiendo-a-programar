# Eliminar un contacto por nombre

import json

with open("contactos_tel.json", "r", encoding="utf-8") as f:
    contenido = json.load(f)

nombre = input("Nombre a eliminar: ")

if nombre in contenido:
    del contenido[nombre]

    with open("contactos_tel.json", "w", encoding="utf-8") as f:
        json.dump(contenido, f)

    print("Contacto eliminado.")
else:
    print("Ese contacto no existe.")