# Eliminar todas las líneas vacías de un archivo

with open("renglones.txt", "r", encoding="utf-8") as f:
    contenido = f.readlines()

texto = ""

for linea in contenido:
    sin_espacios = linea.strip()
    if sin_espacios:
        texto += linea

print(texto)

