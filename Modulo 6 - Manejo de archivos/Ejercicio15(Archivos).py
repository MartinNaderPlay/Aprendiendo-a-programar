# Pedir nombres y guardarlos sin duplicados.

lista_nombres = []

while str(input("Desea ingresar nombre? (si/no): ")) == "si":
    lista_nombres.append(str(input("Escriba el nombre: ")))

with open("nombres_unicos.txt", "w", encoding="utf-8") as f:
    for nombre in set(lista_nombres):
        f.write(f"{nombre}\n")