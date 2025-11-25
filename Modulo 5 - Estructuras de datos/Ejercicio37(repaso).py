# Contar elementos
# Escribe un función que reciba una lista y devuelva cuántos elementos tiene. 

def cantidadElementos(cantidadLista):
    cantidad = len(cantidadLista)
    return cantidad

lista = ["Juan", "Lucas", "Leopoldo", "Fulanito", "Fulanoto"]

print(f"La lista tiene {cantidadElementos(lista)} elementos.")