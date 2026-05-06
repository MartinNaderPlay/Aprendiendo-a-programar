# Escribir un archivo binario simple (wb)

texto = "Hola, cómo estás?"

with open("saludo_binario.bin", "wb") as f:
    f.write(texto.encode("utf-8"))

