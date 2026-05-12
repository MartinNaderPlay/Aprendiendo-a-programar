# Calcula el precio total leyendo el json

import json

precio_total = 0

with open("lista_productos_precios.json", "r", encoding="utf-8") as f:
    contenido = json.load(f)

for element in contenido:
    for clave, valor in element.items():
        precio_total += valor

print(f"El precio total de los productos son: {precio_total}")


