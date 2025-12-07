# Inventario estilo RPG
# Diccionario con objetos
# {"Poción" : 3, "Espada": 1, "Flechas", 2}
# Función para usar objeto (restar cantidad). Si llega a 0, eliminar

inventario_objetos = {
    "Poción" : 3,
    "Espada" : 1,
    "Flechas" : 2
}

def usar(objeto):
    if objeto in inventario_objetos:
        inventario_objetos[objeto] -= 1
        if inventario_objetos[objeto] == 0:
            del inventario_objetos[objeto]

def mostrar():
    for objeto, cantidad in inventario_objetos.items():
        print(f"Quedan {cantidad} unidades de {objeto}")

while str(input("Usar objeto (si/no): ")) == "si":
    usar(str(input("Qué objeto vas a usar? (Poción/Espada/Flechas): ")))
    mostrar()