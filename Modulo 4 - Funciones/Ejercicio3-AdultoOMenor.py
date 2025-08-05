def menor_de_edad():
    print(f"{nombre}, eres menor de edad")

def adulto():
    print(f"{nombre}, eres adulto")

nombre = str(input("ingrese su nombre: "))
edad = int(input("ingrese su edad: "))

if edad >= 18:
    adulto()
else:
    menor_de_edad()