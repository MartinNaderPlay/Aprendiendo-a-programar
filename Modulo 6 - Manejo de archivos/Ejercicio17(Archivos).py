# Crear un archivo y reemplazar una palabra por otra

texto = "Hola me llamo marcos y tengo 30 años."

with open("texto_corregir.txt", "w", encoding="utf-8") as f:
    f.write(texto)

with open("texto_corregir.txt", "r", encoding="utf-8") as f:
    contenido = f.readline()
    print(contenido)
    
palabra_error = str(input("Escriba la palabra que desea quitar: "))
texto_nuevo = []
for palabra in contenido.split():
    if palabra == palabra_error:
        palabra = str(input("Escriba la palabra correcta: "))
        texto_nuevo.append(palabra)
    else:
        texto_nuevo.append(palabra)

texto = " ".join(texto_nuevo)

with open("texto_corregir.txt", "w", encoding="utf-8") as f:
    f.write(texto)

print(texto)