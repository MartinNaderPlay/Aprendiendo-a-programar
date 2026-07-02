# Guardar una tabla (lista de listas) en json y volver a reconstruirla

import json

tabla = [
    [1, 3, 5],
    [2, 4, 8],
    [10, 20, 30]
]

with open("tabla.json", "w", encoding="utf-8") as f:
    json.dump(tabla, f)

with open("tabla.json", "r", encoding="utf-8") as f:
    contenido = json.load(f)

for element in contenido:
    print(f"{element}")
