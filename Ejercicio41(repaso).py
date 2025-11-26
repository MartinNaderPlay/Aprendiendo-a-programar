# Mezcla lista y set
# Verifica cuantos elementos de una lista están en un set

lista = ["Pablo", "Rita", 45, "Marcos", 1, 25, "Lucas"]

conjunto = {4, 90, "Martín", 1, "Iván", 45, "Rita"}

listaC = set(lista)

print("La cantidad de elementos de la lista que están en el set son:", len(listaC&conjunto))