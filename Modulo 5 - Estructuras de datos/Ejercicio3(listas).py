# 1. Crea una lista con al menos 8 elementos (pueden ser número, letras o mezclados).
# 2. Muestra los primeros 3 elementos con slicing.
# 3. Muestra los últimos 2 elemenots con slicing.
# 4. Muestra los elementos del índice 2 al 5.
# 5. Muestra toda la lista pero saltando de 2 en 2.


elementosVarios = [4, "e", "m", 9, "h", 14, 24, 30]

print("La lista de todos los elementos es: ", elementosVarios)


print("Los primero 3 elementos de la lista son: ", elementosVarios[:3])

print("Los ultimos 2 elementos de la lista son: ", elementosVarios[-2:])

print("Los elementos del indice 2 al 5 son: ", elementosVarios[2:6])

print("Los elementos de 2 en 2, de la lista son: ", elementosVarios[::2])



