# Leer la lista del ejercicio anterior y mostrar la suma

import json

with open("lista_numeros.json", "r", encoding="utf-8") as f:
    contenido = json.load(f)

print(f"La suma de los elementos de la lista es: {sum(contenido)}")