# Crear un diccionario llamado producto
# Muesta en pantalla: nombre, precio, categoria (una por línea)
# Agrega nueva categoría llamada "portatiles"
# Actualiza el stock restando 3 unidades (Simula una ventana)
# Agrega un nuevo dato al dicionario llamado "descuento" con valor 10 (representando 10%)
# Calcula precio final aplicando descuento y muéstralo
# Elimina la clave "descuento" del diccionario
# Muestra el diccionario final

producto = {
    "Nombre" : "Laptop",
    "Precio" : 1500,
    "Stock" : 10,
    "Categoria" : ["Tecnología", "Computación"]
    }

def mostrarDiccionario(diccionario):
    for clave, valor in producto.items():
        if clave == "Categoria":
            print(f"{clave}: ")
            for linea in valor:
                print(f"  -{linea}")
        else:
            print(f"{clave} : {valor}")

print("-----Diccionarios inicial-----")
mostrarDiccionario(producto)

print("\n-----Agregamos 'portatiles' al diccionario...-----")
producto["Categoria"] += ["Portatiles"]       
mostrarDiccionario(producto)

print("\n-----Restamos 3 unidades del stock...-----")
producto["Stock"] -= 3
mostrarDiccionario(producto)

print("\n-----Aplicamos un descuento del 10%...-----")
producto["Descuento"] = 10
mostrarDiccionario(producto)

print("\n-----El resultado final es:-----")
producto["Precio"] = producto["Precio"] - producto["Precio"] * 0.10
del producto["Descuento"]
mostrarDiccionario(producto)

