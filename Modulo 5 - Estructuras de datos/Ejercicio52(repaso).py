# Inventario con funciones 
# Crea funciones:
# Agregar productos (diccionario, nombre, cantidad)
# Quitar productos (diccionario, nombre, cantidad)
# Mostrar inventario (diccionario)

inventario = {}

def agregar_productos(producto, stock):
    inventario[producto] = stock
    return inventario
    
def quitar_productos(producto, stock):
    inventario[producto] -= stock
    return inventario

while str(input("desea agregar un producto más? (si/no) : ")) == "si":
    agregar_productos(str(input("Agregue productos: ")), int(input("Cantidad: ")))
    print("-----------------------")

print("-----------------------")
while str(input("desea eliminar productos? (si/no) : ")) == "si":
    quitar_productos(str(input("Eliminar productos: ")), int(input("Cantidad: ")))
    print("-----------------------")

for producto, stock in inventario.items():
    print(f"Hay {stock} uidades de {producto}.")