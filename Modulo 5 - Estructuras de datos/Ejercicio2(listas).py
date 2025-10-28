# Crear una lista con 6 números y hacar lo siguiente:
# 1. Muestre todos los elementos usando un for.
# 2. Imprima cuántos elementos tiene la lista.
# 3. Calcula y muestra la suma, el mayor y el menor, número.
# 4. Pregunta al usuario (con input) un número y verifica si está dentro de la lista.

listaNumeros = [3, 4, 8, 9, 11, 16]

print("Los elementos de la lista son: ",)

for numero in listaNumeros:
    print(numero)

print("Los cantidad de elementos de la lista son:", len(listaNumeros))

print("La suma de los numeros de la lista es:", sum(listaNumeros))

print("El número mayor de la lista es el:", max(listaNumeros))

print("El número menor de la lista es el:", min(listaNumeros))


numeroUsuario = int(input("Ingrese un número: "))

if numeroUsuario in listaNumeros:
    print("El número ingresado está dentro de la lista")
else:
    print("El número ingresado no está dentro de la lista")


