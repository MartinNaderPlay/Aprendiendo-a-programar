# Crear un archivo que registre cada ejecución del programa

try:
    with open("eje_count.txt", "r", encoding="utf-8") as f:
        contenido = f.readline()
    nuevo_num = int(contenido)
    nuevo_num += 1
    num_act = str(nuevo_num)
    print(f"El número de ejecuciones realizadas es: {num_act}")
    with open("eje_count.txt", "w", encoding="utf-8") as f:
        f.write(num_act)
except FileNotFoundError:
    with open("eje_count.txt", "w", encoding="utf-8") as f:
        f.write("1")
        print("Esta es la primera ejecución del programa")

