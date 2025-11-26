# Actualiza Stock
# Crea un diccionario Stock {"Manzana" : 10, "Banana" : 5, "Pera" : 2}
# Disminuye 2 manzanas y agrega 3 peras

frutas = {
    "Manzana" : 10,
    "Banana" : 5,
    "Pera" : 2
}

print("El stock inicial de frutas es:")
for clave, valor in frutas.items():
    print(f"{clave}: {valor}")

frutas["Manzana"] -= 2
frutas["Pera"] += 3

print("El stock actualizado de frutas es:")

for clave, valor in frutas.items():
    print(f"{clave}: {valor}")