# Usando la lista final de amigos del ejercicio 5 realizar lo siguiente:
# Eliminar a "Roberto" con remove()
# Quitar el ultimo amigo con pop()
# Borra el primero amigo con del
# Mostrar la lista en cada paso para ir viendo los resultados

listaAmigos = ["José", "Roberto", "Marcos", "Pablo", "Nahuel", "Lucas", "Patricio"]

print("La lista principal es: ", listaAmigos)
 
listaAmigos.remove("Roberto")

print("La lista de amigos sin Roberto queda: ", listaAmigos)

listaAmigos.pop()

print("La lista de amigos eliminando el ultimo elemento queda: ", listaAmigos)

del listaAmigos[0]

print("La lista de amigos borrando el primer elemento queda: ", listaAmigos)

