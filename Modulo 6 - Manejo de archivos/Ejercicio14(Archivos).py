# Detectar si un archivo existe (usar try-except)

archivo = input("ingrese el nombre del archivo: ")

try:
    with open(archivo, "r", encoding="utf-8") as f:
        contenido = f.read()
        print(f"Se encontro el contenido y el mismo muestra lo siguiente: \n{contenido}")
except FileNotFoundError:
    print("No se encontro ningun contenido")