# Sobreescribir un archivo con contenido nuevo

with open("archivo_vacío.txt", "w", encoding="utf-8") as f:
    f.write(str(input("Escriba el texto con el que reemplazara el archivo anterior: ")))