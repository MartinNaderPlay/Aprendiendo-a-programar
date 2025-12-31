# Leer el archivo del ejercicio anterior y mostrarlos multiplicado por 2.

with open("numeros.txt", "r", encoding="utf-8") as f:
    contenido = f.readlines()

for element in contenido:
    element.strip()
    element = int(element)
    print(element*2)



