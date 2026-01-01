# Pedir un texto al usuario y guardarlo en un archivo.

texto = str(input("Escriba un texto para guardar: "))

with open("texto_usuario.txt", "w", encoding="utf-8") as f:
    f.write(texto)




