# Convertir un parrafo a mayusculas y guardarlo en otro archivo

with open("parrafo.txt", "r", encoding="utf-8") as f:
    contenido = f.read()

with open("parrafo_mayusculas.txt", "w", encoding="utf-8") as f:
    en_mayusculas = contenido.upper()
    f.write(en_mayusculas)

