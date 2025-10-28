# Crea una lista de números [8, 3, 6, 1, 9, 3, 5]
# Mostra la lista original.
# Ordenala con sort()
# Ordenala de mayor a menor con sort(reverse=True).
# Mostrá la posición del número 6 con index().
# Contá cuántas veces aparece el número 3 con count().

listaNumeros = [8, 3, 6, 1, 9, 3, 5]

print("La lista original de números es: ", listaNumeros)

listaNumeros.sort()

print("La lista ordenada de números es: ", listaNumeros)

listaNumeros.sort(reverse=True)

print("La lista ordenada de forma invertida es: ", listaNumeros)

listaNumeros.index(9)

print("El número 9 está en la posicion", listaNumeros.index)

