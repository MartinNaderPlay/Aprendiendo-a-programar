texto = "Hola me llamo marcos"
print(texto)
print(texto.split())
nuevo_texto = []
for palabra in texto.split():
    if palabra == "marcos":
        palabra = "martin"
        nuevo_texto.append(palabra)
    else:
        nuevo_texto.append(palabra)
print(" ".join(nuevo_texto))