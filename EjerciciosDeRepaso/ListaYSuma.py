# Crear una lista de numero y luego una funcion que sume los elementos de dicha lista

listaDeNumeros = [1, 3, 7, 10, 18]

def sumarLista(x):
    contador = 0
    for numero in x:
        contador += numero
    return contador
    

print ("El resultado de los elementos de la lista sumados es de:", sumarLista(listaDeNumeros))

