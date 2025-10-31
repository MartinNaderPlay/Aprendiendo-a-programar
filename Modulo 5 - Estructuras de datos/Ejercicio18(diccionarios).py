# Hacer un progrma que administre el inventario de una tienda con cada producto representado por nombre de producto, precio y stock
# Crear una lista con tres productos
# Muestra todos los productos con su nombre, precio y stock
# Agrega un nuevo producto al inventario
# Aumenta el stock del segundo producto en 20 unidades
# Disminuye el stock del tercer producto en 10 unidades
# Calcula e imprime el valor total del inventario, sumando (precio x stock) de todos los productos
# Finalmente, muestra la lista actualizada de productos con su información 

productos = [
    {"Nombre" : "Galletas saladas", "Precio" : 1900, "Stock" : 15},
    {"Nombre" : "Lata de atún", "Precio" : 3800, "Stock" : 8},
    {"Nombre" : "Yogur", "Precio" : 1250, "Stock" : 21}
]

print("Lista de precios y stock de productos:\n")
for producto in productos:
    for clave, valor in producto.items():
        print(f"{clave} : {valor}")
    print()

productos.append({"Nombre" : "Jugo de manzana", "Precio" : 2100, "Stock" : 5})

productos[1]["Stock"] = productos[1]["Stock"] + 20

productos[2]["Stock"] = productos[2]["Stock"] - 10


total = 0

for producto in productos:
    total += ( producto["Stock"] * producto["Precio"] )

print("El capital total de todo los productos es: ", total)
print()

print("La lista detallada de los productos es:\n")
for producto in productos:
    for clave, valor in producto.items():
        print(f"{clave}: {valor}")
    print()