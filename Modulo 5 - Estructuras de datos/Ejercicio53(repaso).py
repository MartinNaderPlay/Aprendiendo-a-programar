# Filtrar diccionario 
# Dado un diccionario de productos y precios, retornar otro diccionario solo con los productos que cuesten más de 1000.

productos_precios = {
    "Harina" : 1500,
    "Leche" : 2100,
    "Galletas" : 900,
    "Gomitas" : 50,
    "Alfajor" : 1000,
    "Dulce de leche": 3500,
    "Caldo de verduras" : 250,
    "Agua chica" : 850
}

productos_mas_de_mil = {}

for producto, precio in productos_precios.items():
    if precio > 1000:
        productos_mas_de_mil[producto] = precio

print("\nLista total de productos\n")

for producto, precio in productos_precios.items():
    print(f"El producto {producto}, cuesta: ${precio}")

print("\nLista de productos con valor mayor a 1000\n")

for producto, precio in productos_mas_de_mil.items():
    print(f"El producto {producto}, cuesta: ${precio}")