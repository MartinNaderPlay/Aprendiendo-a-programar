# Crear archivo con un parrafo y contar palabras.

cantidad_palabras = 0

with open("parrafo.txt", "w", encoding="utf-8") as f:
    f.write(str(input("Escriba un parrafo: ")))

with open("parrafo.txt", "r", encoding="utf-8") as f:
    contenido = f.readline()
    for element in contenido.split():
        cantidad_palabras += 1
    print("La cantidad de palabras del parrafo son:", cantidad_palabras)

    