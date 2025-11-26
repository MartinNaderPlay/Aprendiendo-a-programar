# Pedir 5 números al usuario y devolver la lista invertida

listaNumeros = [
    int(input("Ingrese el primer número: ")),
    int(input("Ingrese el segundo número: ")),
    int(input("Ingrese el tercer número: ")),
    int(input("Ingreseel cuarto número: ")),
    int(input("Ingrese el último número: "))
    ]

print("La lista invertida de los números ingresados es: ", listaNumeros[::-1])