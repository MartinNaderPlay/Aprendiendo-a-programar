# Guardar 5 nombres ingresados por el usuario

def ingresar(nombre):
    with open("nombres.txt", "a", encoding="utf-8") as f:
        f.write(f"{nombre}\n")

for ingreso in range(5):
    ingresar(str(input("Escriba un nombre: ")))