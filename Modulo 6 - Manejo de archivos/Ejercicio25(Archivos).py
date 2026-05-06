# Leer un archivo binario simple (rb)

with open("saludo_binario.bin", "rb") as f:
    contenido = f.readline()

print(contenido)