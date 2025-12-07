# Carrito de compras
# Diccionario con productos y precios
# El usuario va agregando productos a una lista
# Mostrar total 

productos_precios = {}

total = 0

def agregar(producto, precio):
    productos_precios[producto] = precio

while  str(input("Desea ingresar un producto a la lista? (si/no) :")) == "si":
    agregar(str(input("Ingrese el noombre del producto: ")), int(input("Ingrese el valor del producto: ")))

print("--------------------\n-Carrito de compras-\n--------------------")
for producto, precio in productos_precios.items():
    print(f"{producto} : ${precio}")
    total += precio
print(f"--------------------\nTotal: ${total}\n--------------------")


