# Juntar dos archivos de texto en uno solo.

with open("parrafo.txt", "r", encoding="utf-8") as minusculas, \
    open("parrafo_mayusculas.txt", "r", encoding="utf-8") as mayusculas:
    contenido1 = minusculas.read()
    contenido2 = mayusculas.read()

with open("texto1+texto2.txt", "w", encoding="utf-8") as f:
    f.write(contenido1+contenido2)