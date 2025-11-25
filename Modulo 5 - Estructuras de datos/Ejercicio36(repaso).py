# Mezclar datos
# Tienes una lista de nombres y una lista de edades. Crea un diccionario juntándolas:

nombres = ["Ana", "Luis", "Pedro"]

edades = [20, 25, 30]

nombresEdades = {
    nombres[0] : edades[0],
    nombres[1] : edades[1],
    nombres[2] : edades[2]
}

print("La lista de nombres y edades es:")

for clave, valor in nombresEdades.items():
    print(f"{clave}: {valor}")