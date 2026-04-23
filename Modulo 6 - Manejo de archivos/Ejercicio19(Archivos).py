# Leer un archivo y mostrar solo las lineas que contengan una palabra especifica

with open("lista_jugadores.txt", "r", encoding="utf-8") as f:
    contenido = f.readlines()

palabra_especifica = input(str("Ingrese una palabra para mostrar toda su linea: "))

for linea in contenido:
    if palabra_especifica in linea:
        print(linea)

