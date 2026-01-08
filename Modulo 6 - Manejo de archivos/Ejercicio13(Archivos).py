# Crear un archivo de notas (números) y calcular el promedio

def ingresar(nota):
    with open("notas.txt", "a", encoding="utf-8") as f:
        f.write(f"{nota}\n")

def promedio():
    with open("notas.txt", "r", encoding="utf-8") as f:
        contenido = f.readlines()
        notas = []
        for elemento in contenido:
            notas.append(int(elemento.strip()))
    promedio = sum(notas)/len(notas)
    return print(f"El promedio de las notas ingresadas es: {promedio}")

while str(input("Desea ingresar una nota? si/no: ")) == "si":
    ingresar(int(input("Ingrese una nota: ")))
promedio()