# Crear una lista con cinco numeros y guardarlos en json

import json 

lista_numeros = [4, 8, 43, 2, 9]

with open("lista_numeros.json", "w", encoding="utf-8") as f:
    json.dump(lista_numeros, f)
