# Crear un archivo json con tu nombre y edad.

import json

nombre = "Martín"
edad = 31

with open("nombre_edad.json", "w", encoding="utf-8") as f:
    f.write(f"Nombre: {nombre}\nEdad: {edad}")