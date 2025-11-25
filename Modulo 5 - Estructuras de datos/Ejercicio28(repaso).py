# Tupla a lista
# Dada la tupla (10, 20, 30) convertirla en una lista, agregar un elemento y convertirla a tupla, nuevamente.

numerosTupla = (10, 20, 30)

numerosLista = list(numerosTupla)

numerosLista.append(40)

numerosTupla = tuple(numerosLista)

print(numerosTupla)