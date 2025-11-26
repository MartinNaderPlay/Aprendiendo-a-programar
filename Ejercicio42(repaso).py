# Palabras únicas
# Dado un texto, muestra todas las palabras sin repetir (usar set)

texto = "Había una vez una casita blanca y en ella una taza de color azul"

palabras = texto.split()

conjuntoPalabras = set(palabras)

print("Las palabras sin repetir del texto son:\n")

for palabra in conjuntoPalabras:
    print(palabra)