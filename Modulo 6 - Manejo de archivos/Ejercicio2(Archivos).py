# Leer el archivo del ejercicio 1 y mostrarlo en pantalla 

with open("saludo.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
    print(contenido)