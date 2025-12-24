# Crear un archivo y escribir los numeros del 1 al 10, uno por linea 

with open("numeros.txt", "w", encoding="utf-8") as f:
    for numero in range(1, 11):
        f.write(f"{numero}\n")
