# Pedir al usuario que ingrese un numero y confirmar si es un numero primo.

numero = int(input("Ingresar un numero: "))

if numero < 2:
    print("El numero", numero, "no es un numero primo")
else:
    raizNumero = numero ** 0.5
    divisor = 2
    es_primo = True  # asumimos que sí, hasta que encontremos un divisor

    while divisor <= raizNumero:
        if numero % divisor == 0:
            es_primo = False
            break  # ya encontramos un divisor, no hace falta seguir
        divisor += 1

    if es_primo:
        print("El numero", numero, "es un numero primo")
    else:
        print("El numero", numero, "no es un numero primo")





