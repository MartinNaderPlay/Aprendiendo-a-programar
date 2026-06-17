# Crear un programa que guarde sesiones con contador: cada vez que se abre, suma 1

import json

sesiones = []

try:
    with open("sesiones.json", "r", encoding="utf-8") as f:
        contenido = json.load(f)
        for element in contenido:
            sesiones.append(element)
        pivot = sesiones[-1].copy()
        pivot["sesion"] += 1
        pivot["asunto"] = str(input("Escriba los detalles de la sesion:"))
        sesiones.append(pivot)
    with open("sesiones.json", "w", encoding="utf-8") as f:
        json.dump(sesiones, f)
except FileNotFoundError:
    with open("sesiones.json", "w", encoding="utf-8") as f:
        sesiones.append({"sesion": 1, "asunto": str(input("Escriba el detalle de la primera sesion: "))})
        json.dump(sesiones, f)