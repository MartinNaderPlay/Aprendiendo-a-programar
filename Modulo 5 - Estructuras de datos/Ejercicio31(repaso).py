# Crear diccionario
# Crea un diccionario con: Nombre, edad y país. Imprimelo

datosPersona = {
    "Nombre" : "Martín",
    "Edad" : 30,
    "País" : "Argentina"
}

print("Los datos del diccionario son:")

for clave, valor in datosPersona.items():
    print(f"{clave}: {valor}")