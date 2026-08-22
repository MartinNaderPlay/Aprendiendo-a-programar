# Crear una copia de seguridad de cualquier archivo

archivo = str(input("Escriba el nombre del archivo que quiere copiar: "))

with open(archivo + ".txt", "r", encoding="utf-8") as f:
    contenido = f.read()

with open("copia_seguridad_archivo_largo.txt", "w", encoding="utf-8") as f:
    f.write(contenido)