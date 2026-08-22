# Programa que analice un archivo largo y muestre:
# Cantidad de lineas
# Cantidad de palabras
# Palabra más repetida

from collections import Counter

renglones = 0
palabras = 0
repetidas_por_linea = []

from collections import Counter

renglones = 0
todas_las_palabras = [] 

with open("archivo_largo.txt", "r", encoding="utf-8") as f:
    contenido_renglones = f.readlines() 

    for linea in contenido_renglones:
        renglones += 1
        palabras_de_linea = linea.split()
        todas_las_palabras.extend(palabras_de_linea) 

cantidad_palabras = len(todas_las_palabras)

conteo = Counter(todas_las_palabras)
palabra_mas_repetida = conteo.most_common(1)

print(f"Cantidad de lineas: {renglones}")
print(f"Cantidad de palabras: {cantidad_palabras}")
print(f"Palabra mas repetida: {palabra_mas_repetida}")

