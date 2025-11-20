# Crea un diccionario llamado productos con: nombre, precio y un conjunto inicial de etiquetas, ejemplo:
# {"Teconología", "portatil", "oferta"}
# Muestra todas las etiquetas en pantalla, una por linea
# Agrega tres nuevas etiquetas usando: 
# add() 
# update() con un iterable
# Intenta eliminar una etiqueta repetida (para ver que el set la ignora)
# Elimina una etiqueta existente usando remove()
# Elimina otra etiqueta usando discard() (elige una que NO exista)
# Crea un segundo conjunto llamado etiquetas_prohibidas, por ejemplo:
# {"oferta", "importado", "reacondicionado"}
# Quita del producto todas las etiquetas que estén en etiquetas_prohibidas (usa difference_update())
# Muestra el diccionario completo al final.

producto = {
    "Nombre" : "Alfajor",
    "Precio" : 1800,
    "Etiquetas" : {"Comestibles", "Postres", "Oferta"}
}

def imprimir(diccionario):
    for clave, valor in producto.items():
        if clave == "Etiquetas":
            print(f"{clave}:")
            for linea in valor:
                print(f"   -{linea}")
        elif clave == "EtiquetasProhibidas":
            print(f"{clave}:")
            for linea in valor:
                print(f"   -{linea}")    
        else:
            print(f"{clave}: {valor}")
        
imprimir(producto)        

producto["Etiquetas"].add("Golosinas")
producto["Etiquetas"].update({"Dulces", "MiniTorta", "Postres"}) 
producto["Etiquetas"].remove("Dulces")
producto["Etiquetas"].discard("Comida")
producto["EtiquetasProhibidas"] = {"Descuento", "Estropeado", "Artesanal"}

imprimir(producto)

producto["EtiquetasProhibidas"].difference_update({"Descuento", "Estropeado", "Artesanal"})

print("Diccionario final")

imprimir(producto)