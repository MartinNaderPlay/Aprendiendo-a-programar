2# Buscar en lista
# Escribe una función que busque un número dentro de una lista. Devuelve True o False.

def check(num):
    return print(num.issubset(setNumeros))

listaNumeros = [2, 6, 7, 9, 15]

numeroIngreso = [int(input("Escribe un numero para buscar en la lista: "))]

setNumeros = set(listaNumeros)
setNumeroIngreso = set(numeroIngreso)

check(setNumeroIngreso)