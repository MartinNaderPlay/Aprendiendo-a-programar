# Leer los nombres del ejericio anterior y mostrarlos alfabeticamente

with open("nombres.txt", "r", encoding="utf-8") as f:
    contenido = f.readlines()
    ordenadas = []
    for elemento in contenido:  
        ordenadas.append(elemento.strip())
    print("\nLista de nombres ordenados alfabeticamente:\n")
    for nombre in sorted(ordenadas):
        print(nombre)