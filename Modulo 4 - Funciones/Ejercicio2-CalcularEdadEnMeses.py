def edad_meses():
    resultado = edad_años * 12
    return resultado

edad_años = int(input("ingrese su edad: "))

print("Usted ha vivido", edad_meses(), "meses")
