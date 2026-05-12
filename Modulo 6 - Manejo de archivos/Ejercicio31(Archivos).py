# Agregar un contacto nuevo al json existente

import json

with open("contactos_tel.json", "r", encoding="utf-8") as f:
    contenido = json.load(f)

with open("contactos_tel.json", "w", encoding="utf-8") as f:
    contenido["Pablo"] = 23423942834
    json.dump(contenido, f)