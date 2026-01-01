# Leer un archivo y mostrarlo sin saltos de linea

with open("verso.txt", "r", encoding="utf-8") as f:
    texto_sin_saltos = ""

    for linea in f:
        texto_sin_saltos += linea.strip()
        texto_sin_saltos += " "

print(texto_sin_saltos)


