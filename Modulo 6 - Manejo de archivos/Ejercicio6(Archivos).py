# Contar cuántas lineas tiene un archivo.

with open("numeros.txt", "r", encoding="utf-8") as f:
    contenido = f.readlines()

print(len(contenido))