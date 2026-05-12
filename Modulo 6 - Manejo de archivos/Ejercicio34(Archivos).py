# Guardar una lista de diccionarios (producto con precio) 

import json

producto_precio = [
    {"Fideos": 2500},
    {"Harina": 1200},
    {"Soda": 1900},
    {"Chocolate": 3300}
]

with open("lista_productos_precios.json", "w", encoding="utf-8") as f:
    json.dump(producto_precio, f)