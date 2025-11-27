# Filtrar lista
# Dada una lista de números, cree otra con solo los pares

listaNumeros = [4, 32, 3, 7, 9, 40, 64, 1, 5, 21]

listaNumPares = []

for numero in listaNumeros:
    if numero % 2 == 0:
        listaNumPares.append(numero)

print("La lista de numerós es: ", listaNumeros)
print("Los números pares de la lista son: ", listaNumPares)