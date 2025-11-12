# Mostrar un conjunto con los nombres de 5 países y mostrarlo por pantalla.
# Agregar un país al conjunto anterior.
# Eliminar un país (elegir).
# Crear dos conjuntos de números y mostrar: su unión, su intersección, su diferencia, su diferencia simétrica.
# Crear una lista con elementos repetidos y convertirla a conjunto para eliminar duplicados.

paises = {"Argentina", "Canadá", "Bélgica", "Japón", "Italia"}

print("Los paises del conjunto son:", paises)

paises.add("Uruguay")

paises.remove("Canadá")

print("\nLista final de paises:", paises)

numerosA = {2, 4, 6, 8}
numerosB = {1, 3, 6, 9}

print("\nLa uninón de los conjuntos es:", numerosA|numerosB)
print("\nLa intersección de los conjuntos es:", numerosA&numerosB)
print("\nLa diferencia de los conjuntos es:", numerosA-numerosB)
print("\nLa diferencia simétrica de los conjuntos es:", numerosA^numerosB)

listaCompras = ["Harina", "Manteca", "Uvas", "Arroz", "Leche", "Manteca", "Naranjas", "Uvas"]

listaConjunto = set(listaCompras)

print("\nEl conjunto de la lista de compras es:", listaConjunto)