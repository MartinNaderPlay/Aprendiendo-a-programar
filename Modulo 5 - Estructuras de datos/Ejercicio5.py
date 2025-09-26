# Crear una lista con 3 nombres de amigos.
# Agregar un cuarto amigo al final con append()
# Agrega otro en la segunda posición con insert()
# Extiende la lista con otros 2 nombres de una lista aparte
# Mostrá la lista final

listaAmigos = ["José", "Marcos", "Pablo"]

print("La lista de amigos principal es: ", listaAmigos)

listaAmigos.append("Nahuel")
listaAmigos.insert(1, "Roberto")

listaAmigos2 = ["Lucas", "Patricio"]

listaAmigos.extend(listaAmigos2)

print("La lista de amigos final es: ", listaAmigos)